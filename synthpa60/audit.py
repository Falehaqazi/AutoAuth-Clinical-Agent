# -*- coding: utf-8 -*-
"""Automated consistency audit: for every criterion, does the note DISCUSS the
topic when the vector says TRUE/FALSE, and STAY SILENT when it says ABSENT?
The ABSENT check is the one that matters most -- an 'undocumented' criterion the
note actually mentions silently breaks the MORE_INFO label."""
import json, re
from collections import defaultdict

# topic keyword sets per policy criterion
KW = {
"P01": {"R1": ["back pain", "weeks", "months", "duration"],
        "R2": ["physical therapy", "physiotherap", "supervised therapy", "PT "],
        "A1": ["weakness", "reflex", "sensation", "deficit", "power"],
        "A2": ["weight loss", "fever", "night sweat", "malignancy", "bowel", "bladder", "red flag"],
        "X1": ["previous", "prior", "performed at this institution", "no previous", "no prior"]},
"P02": {"R1": ["radiograph", "Kellgren", "joint space", "osteophyte"],
        "R2": ["conservative", "physical therapy", "injection", "NSAID", "naproxen", "meloxicam", "celecoxib"],
        "R3": ["stairs", "walk", "dressing", "activities", "cannot", "unable", "assistance"],
        "X1": ["infection", "fever", "erythema", "effusion"],
        "X2": ["body mass index", "BMI", "weight management"]},
"P03": {"R1": ["examination", "neurological", "deficit", "seizure", "papilloedema", "sign"],
        "A1": ["new onset", "headache", "deficit", "palsy"],
        "A2": ["preventive", "propranolol", "topiramate", "amitriptyline", "refractory", "migraine"],
        "A3": ["mass", "lesion", "CT head", "midline shift", "oedema"],
        "X1": ["surveillance", "asymptomatic", "symptomatic"]},
"P04": {"R1": ["spondylolisthesis", "instability", "flexion-extension", "translation", "anterolisthesis"],
        "R2": ["non-operative", "physical therapy", "injection", "months", "years"],
        "R3": ["concordant", "correlat", "distribution", "nerve root block", "localise"],
        "X1": ["smok", "nicotine", "tobacco"],
        "X2": ["DEXA", "T-score", "osteoporo"]},
"P05": {"R1": ["body mass index", "BMI", "weighs", "height"],
        "R2": ["weight management programme", "supervised", "dietitian", "months"],
        "R3": ["psychological evaluation", "PsyD", "clearance", "cleared"],
        "X1": ["alcohol", "tobacco", "substance", "toxicology"],
        "X2": ["pregnan", "contracept", "intrauterine", "conceive", "male"]},
"P06": {"R1": ["snoring", "apnoea", "sleepiness", "Epworth", "witnessed"],
        "A1": ["heart failure", "lung disease", "COPD", "neuromuscular", "ejection fraction", "FEV1"],
        "A2": ["home sleep", "technically inadequate", "aborted", "negative", "home study"],
        "X1": ["insomnia", "sleep onset", "initiating sleep", "rumination"]},
"P07": {"R1": ["sleep study", "polysomnography", "home sleep apnoea test", "no sleep study"],
        "R2": ["apnoea hypopnoea index", "AHI", "events per hour"],
        "R3": ["face to face", "clinical evaluation", "prior to this order", "in advance of this order"],
        "X1": ["tolerat", "interface", "intoleran"]},
"P08": {"R1": ["radiograph", "joint space", "osteoarthritis", "avascular", "fracture", "sclerosis"],
        "R2": ["conservative", "physical therapy", "physiotherapist", "injection", "months", "weeks"],
        "A1": ["block", "metres", "walk", "ambulat"],
        "A2": ["night", "sleep", "wakes", "nocturnal"],
        "X1": ["infection", "fever", "erythema", "CRP"]},
"P09": {"R1": ["chest", "angina", "dyspnoea", "symptom", "pain", "no symptom"],
        "R2": ["pretest probability", "pooled cohort", "percent"],
        "X1": ["invasive coronary angiography", "obstructive coronary"],
        "X2": ["glomerular filtration", "creatinine", "eGFR"]},
"P10": {"R1": ["MRI", "full thickness", "partial thickness", "tear", "imaging"],
        "R2": ["conservative", "physical therapy", "weeks", "injection"],
        "A1": ["strength", "weakness", "empty can", "drop arm", "lag sign"],
        "A2": ["traumatic", "fall", "injury", "years of age", "years old", "insidious"],
        "X1": ["arthrit", "arthropathy", "joint space", "acromiohumeral", "Hamada"]},
"P11": {"R1": ["activities of daily living", "toileting", "bathing", "meal preparation", "within the home"],
        "R2": ["specialty", "mobility evaluation", "OTR", "PT, DPT", "therapist"],
        "R3": ["operat", "joystick", "caregiver", "driving assessment", "safe"],
        "X1": ["manual wheelchair", "walker", "rollator", "propel"],
        "X2": ["home assessment", "doorway", "level access", "residence", "modification", "dwelling"]},
"P12": {"R1": ["Wagner", "ulcer", "grade"],
        "R2": ["wound care", "debridement", "offloading", "days", "weeks"],
        "R3": ["ankle brachial", "perfusion", "transcutaneous oxim", "vascular assessment"],
        "X1": ["pneumothorax", "chest radiograph"]},
}

cases=[json.loads(l) for l in open("synthpa60/cases.jsonl")]
pols={p["policy_id"]:p for p in (json.loads(l) for l in open("synthpa60/policies.jsonl"))}

fails=[]; absent_ok=0; present_ok=0
for c in cases:
    note=c["clinical_note"].lower()
    kws=KW[c["policy_id"]]
    for cid,val in c["criteria"].items():
        terms=[t.lower() for t in kws.get(cid,[])]
        if not terms: continue
        hit=any(t in note for t in terms)
        if val=="undocumented":
            if hit:
                hits=[t for t in terms if t in note]
                fails.append(f"{c['case_id']} {c['policy_id']}.{cid} marked ABSENT but note mentions {hits}")
            else: absent_ok+=1
        else:
            if not hit:
                fails.append(f"{c['case_id']} {c['policy_id']}.{cid} marked {val} but note never discusses the topic")
            else: present_ok+=1

print(f"criteria checked: {absent_ok+present_ok+len(fails)}")
print(f"  TRUE/FALSE criteria where the note discusses the topic: {present_ok}")
print(f"  ABSENT criteria where the note stays silent:            {absent_ok}")
print(f"  failures: {len(fails)}")
for f in fails: print("   ", f)
