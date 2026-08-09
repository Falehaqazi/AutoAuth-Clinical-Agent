# SynthPA-60 validation worksheet

For each case: read the note, confirm each line, tick the box.
A case passes only if every criterion line is correct **and** the note
never states or implies a decision.

60 cases. Nine are marked FLAGGED — the automated audit found
the note discusses a criterion marked ABSENT. In most of these the note
says the information *could not be established*, which is arguably the
right way to render a documentation gap in realistic prose. You are the
one who decides whether that reads as absent or as a negative finding.

---

## C001 — Group 2 power wheelchair (HCPCS K0823)

stratum `retrieval_distractor` · gold **APPROVED**

> Patient: Margaret Ellison. MRN: 4471908. DOB: 03/17/1951. Referring clinician: A. Okafor, MD. Requesting HCPCS K0823, Group 2 power wheelchair. Patient has advanced multiple sclerosis with progressive lower extremity weakness. She is unable to traverse the distance from her bedroom to her kitchen or bathroom without stopping, and cannot complete dressing, toileting, or meal preparation within the home on her own. A manual wheelchair was trialled over eight weeks; bilateral upper extremity weakness and shoulder fatigue prevented her from self-propelling more than a few feet, and it does not meet her needs in the home. Occupational therapy specialty mobility evaluation was completed 11 March 2026 by K. Raghavan, OTR/L. Patient operated a demonstration unit with correct joystick control, obstacle avoidance, and stopping, and was assessed as safe to drive independently. Home assessment documents 36 inch doorways throughout and a ramped entry; the residence accommodates the device without modification. Separately, she remains on nightly CPAP for previously diagnosed obstructive sleep apnoea, stable and unrelated to this request.

Confirm:

- [ ] **TRUE** — Mobility limitation preventing completion of activities of daily living within the home  
      *note must state this is met*
- [ ] **TRUE** — Specialty evaluation by a licensed therapist completed within the previous 6 months  
      *note must state this is met*
- [ ] **TRUE** — Patient demonstrates capacity to operate the device safely, or a caregiver is available to operate it  
      *note must state this is met*
- [ ] **FALSE** — A manual wheelchair or lesser mobility device adequately meets the patient's needs  
      *note must state this is NOT met*
- [ ] **FALSE** — Home environment cannot accommodate the device and no modification is planned  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

- [ ] mentions a second unrelated procedure (Continuous positive airway pressure device) that does not affect the criteria

---

## C002 — Lumbar spinal fusion, single level (CPT 22612)

stratum `clear_deny` · gold **DENIED**

> Patient: Dennis Farrow. MRN: 2298315. DOB: 11/02/1968. Referring clinician: L. Mbeki, MD. Requesting CPT 22612, posterolateral lumbar fusion at L4-L5. Flexion-extension radiographs dated 22 January 2026 demonstrate grade 1 degenerative spondylolisthesis at L4-L5 with 5 mm of translation on flexion, consistent with segmental instability at that level. Non-operative management has extended over nine months and included 14 sessions of physical therapy, a structured home exercise programme, NSAIDs, and two epidural steroid injections, without durable benefit. His presenting symptoms are axial low back pain with radiation into the right anterior thigh and groin; examination localises tenderness over the right sacroiliac joint, and provocative sacroiliac testing reproduces his pain. The distribution does not correspond to an L4-L5 radiculopathy and his symptoms do not correlate with the level demonstrated on imaging. Patient is a lifelong non-smoker. DEXA dated 09 December 2025 shows a T-score of negative 0.8. Requesting review for surgical planning.

Confirm:

- [ ] **TRUE** — Radiographic confirmation of spondylolisthesis or segmental instability at the operative level  
      *note must state this is met*
- [ ] **TRUE** — Failed at least 6 months of non-operative management including physical therapy  
      *note must state this is met*
- [ ] **FALSE** — Concordant symptoms correlating with the imaged level  
      *note must state this is NOT met*
- [ ] **FALSE** — Active nicotine use without documented cessation counselling  
      *note must state this is NOT met*
- [ ] **FALSE** — Untreated osteoporosis with T-score below negative 2.5  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C003 — Total knee arthroplasty (CPT 27447)

stratum `borderline` · gold **APPROVED**

> Patient: Yolanda Prieto. MRN: 8830247. DOB: 06/29/1959. Referring clinician: S. Adeyemi, MD. Requesting CPT 27447, total knee arthroplasty, left knee. Weight-bearing radiographs dated 04 February 2026 show definite joint space narrowing, multiple osteophytes, and sclerosis of the medial compartment, read as Kellgren-Lawrence grade 3. Conservative management began 05 November 2025 and has now run three months to the day, comprising naproxen 500 mg twice daily, 12 supervised physical therapy sessions, and one intra-articular corticosteroid injection, with no sustained improvement. She reports difficulty descending stairs, cannot kneel, and has stopped her grocery shopping and gardening because of pain; she now uses a cane for community ambulation. Current weight 118 kg, height 1.63 m, calculated BMI 44.4. She is enrolled in a medically supervised weight management programme with dietitian follow-up every six weeks. No erythema, effusion, or warmth over the joint; no fever; no recent dental or skin infection. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic evidence of advanced osteoarthritis (Kellgren-Lawrence grade 3 or 4)  
      *note must state this is met*
- [ ] **TRUE** — Failed conservative management for at least 3 months including NSAIDs and physical therapy  
      *note must state this is met*
- [ ] **TRUE** — Documented functional limitation affecting activities of daily living  
      *note must state this is met*
- [ ] **FALSE** — Active infection of the joint or of an adjacent surgical site  
      *note must state this is NOT met*
- [ ] **FALSE** — Body mass index of 45 or greater without documented weight management plan  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C004 — Hyperbaric oxygen therapy for diabetic foot ulcer (HCPCS G0277)

stratum `borderline` · gold **APPROVED**

> Patient: Harold Nkemdirim. MRN: 6612094. DOB: 01/23/1954. Referring clinician: P. Vasquez, MD. Requesting HCPCS G0277, hyperbaric oxygen therapy for a chronic diabetic foot ulcer. Patient has type 2 diabetes of 19 years duration. Ulcer over the plantar aspect of the right first metatarsal head, present since November 2025, measures 3.1 by 2.4 cm with probing to tendon and exposed deep tissue without radiographic osteomyelitis, staged as Wagner grade 3. Standard wound care has been delivered for exactly 30 days from 08 July 2026 to 07 August 2026, including four sessions of sharp debridement, total contact casting for offloading, and twice weekly dressing changes; the wound bed has not reduced in area over that interval. Vascular assessment on 30 July 2026 documents an ankle brachial index of 0.91 on the right with triphasic waveforms and transcutaneous oximetry of 42 mmHg periwound, indicating perfusion adequate to support healing. Chest radiograph clear, no pneumothorax. Requesting review.

Confirm:

- [ ] **TRUE** — Wagner grade 3 or higher diabetic foot ulcer documented  
      *note must state this is met*
- [ ] **TRUE** — Failed at least 30 days of standard wound care including debridement and offloading  
      *note must state this is met*
- [ ] **TRUE** — Adequate lower extremity perfusion confirmed by vascular assessment  
      *note must state this is met*
- [ ] **FALSE** — Untreated pneumothorax  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C005 — Total hip arthroplasty (CPT 27130)

stratum `clear_deny` · gold **DENIED**

> Patient: Beatrice Lindqvist. MRN: 5540118. DOB: 08/14/1949. Referring clinician: R. Chaudhry, MD. Requesting CPT 27130, total hip arthroplasty, right hip. AP pelvis and lateral radiographs dated 27 July 2026 demonstrate advanced osteoarthritis of the right hip with complete superolateral joint space obliteration, subchondral cyst formation, and femoral head flattening. Conservative management commenced 19 July 2026, three weeks ago, and consists of paracetamol, a single physical therapy assessment visit, and activity modification; no further therapy has yet been delivered and the trial remains in its early stage. She reports pain that stops her after approximately half a block of walking, and she now uses a walker outdoors. She sleeps through the night without waking from hip pain and reports no nocturnal symptoms. No fever, no wound, no erythema over the hip, and no evidence of local or systemic infection. Inflammatory markers within normal limits. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic evidence of advanced hip osteoarthritis, avascular necrosis, or displaced femoral neck fracture  
      *note must state this is met*
- [ ] **FALSE** — Failed conservative management for at least 3 months, or an acute fracture indication making conservative management inappropriate  
      *note must state this is NOT met*
- [ ] **TRUE** — Pain limiting ambulation to less than one block  
      *note must state this is met*
- [ ] **FALSE** — Night pain disturbing sleep on most nights  
      *note must state this is NOT met*
- [ ] **FALSE** — Active local or systemic infection  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C006 — Lumbar spine MRI without contrast (CPT 72148)  **FLAGGED**

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Tobias Renner. MRN: 3387625. DOB: 05/08/1977. Referring clinician: N. Fontaine, MD. Requesting CPT 72148, MRI of the lumbar spine without contrast. Patient reports low back pain beginning approximately ten weeks ago after lifting at work, persistent since onset without resolution. Pain radiates into the left leg below the knee. On examination there is 4 out of 5 weakness of left ankle dorsiflexion, a diminished left Achilles reflex, and reduced sensation over the left lateral calf and dorsum of the foot, consistent with a focal neurological deficit. Straight leg raise reproduces radicular pain at 40 degrees on the left. He has had no unexplained weight loss, no fever or night sweats, no history of malignancy, and no bowel or bladder dysfunction; saddle sensation is intact. He has had no previous lumbar imaging of any modality. Naproxen and gabapentin have been prescribed. Requesting review for advanced imaging.

Confirm:

- [ ] **TRUE** — Low back pain documented for at least 6 weeks  
      *note must state this is met*
- [ ] **ABSENT** — Completed at least 4 weeks of supervised physical therapy without adequate relief  
      *note must NOT establish this either way*
- [ ] **TRUE** — Focal neurological deficit on examination  
      *note must state this is met*
- [ ] **FALSE** — Red flag features present (unexplained weight loss, fever, history of malignancy, or bowel or bladder dysfunction)  
      *note must state this is NOT met*
- [ ] **FALSE** — Lumbar MRI of the same region performed within the previous 6 months with no interval change in symptoms  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C007 — Coronary computed tomography angiography (CPT 75574)

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Aurelio Santangelo. MRN: 9014772. DOB: 12/05/1963. Referring clinician: J. Whitcombe, MD. Requesting CPT 75574, coronary computed tomography angiography. Patient is a 62 year old man with hypertension controlled on lisinopril, hyperlipidaemia with an LDL of 138 mg/dL on atorvastatin, and a 15 pack year smoking history, quit 2014. There is no family history of premature coronary disease. Applying the pooled cohort equations together with his risk factor profile, his pretest probability of obstructive coronary artery disease is calculated at 14 percent, placing him in the low to intermediate range where anatomic testing is most informative. He has never undergone invasive coronary angiography and has no previously confirmed obstructive coronary disease. Renal function is preserved with a creatinine of 0.9 mg/dL and an estimated glomerular filtration rate of 88 mL/min/1.73m2. No iodinated contrast allergy. Resting heart rate 58, suitable for acquisition. Requesting review.

Confirm:

- [ ] **ABSENT** — Symptoms suggestive of coronary artery disease such as chest pain or anginal equivalent  
      *note must NOT establish this either way*
- [ ] **TRUE** — Low to intermediate pretest probability of obstructive coronary disease documented  
      *note must state this is met*
- [ ] **FALSE** — Known obstructive coronary artery disease already confirmed on invasive angiography  
      *note must state this is NOT met*
- [ ] **FALSE** — Estimated glomerular filtration rate below 30 without nephrology clearance  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C008 — Roux-en-Y gastric bypass (CPT 43644)

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Priscilla Vanterpool. MRN: 7723806. DOB: 09/30/1985. Referring clinician: D. Halvorsen, MD. Requesting CPT 43644, laparoscopic Roux-en-Y gastric bypass. Patient has type 2 diabetes on metformin and semaglutide with a haemoglobin A1c of 8.1 percent, obstructive sleep apnoea on CPAP, and hypertension on amlodipine. She completed a medically supervised weight management programme at this centre from 02 September 2025 through 04 March 2026, six consecutive months, with monthly dietitian visits, exercise physiology sessions, and documented adherence at 22 of 24 scheduled appointments. Preoperative psychological evaluation was performed 19 May 2026 by M. Oyelaran, PsyD, who documented realistic expectations, adequate understanding of postoperative dietary requirements, and cleared her for surgery without reservation. She reports no alcohol use, no tobacco use, and no recreational substance use; a urine toxicology screen on 19 May 2026 was negative. She is not pregnant, has an intrauterine device in place, and states she does not intend to conceive in the next two years. Requesting review.

Confirm:

- [ ] **ABSENT** — Body mass index of 40 or greater, or 35 or greater with an obesity related comorbidity  
      *note must NOT establish this either way*
- [ ] **TRUE** — Documented participation in a supervised weight management programme for at least 6 consecutive months  
      *note must state this is met*
- [ ] **TRUE** — Preoperative psychological evaluation completed and clearance documented  
      *note must state this is met*
- [ ] **FALSE** — Untreated substance use disorder  
      *note must state this is NOT met*
- [ ] **FALSE** — Pregnancy, current or planned within 12 months  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C009 — Brain MRI with contrast (CPT 70553)

stratum `clear_approve` · gold **APPROVED**

> Patient: Colette Bergeron. MRN: 1195438. DOB: 04/11/1990. Referring clinician: T. Adebayo, MD. Requesting CPT 70553, MRI of the brain with and without contrast. Patient presents with a three year history of migraine with aura, now increasing in frequency to 14 headache days per month. Neurological symptoms include recurrent visual scintillations preceding headache and episodic paraesthesia of the right hand lasting 20 to 30 minutes, fully reversible. She has completed sequential preventive trials of propranolol for four months, topiramate for five months at therapeutic dose, and amitriptyline for three months, each titrated appropriately and each without adequate response; headache frequency has not fallen below 12 days per month across these trials, a period exceeding three months of standard preventive therapy. Neurological examination today is entirely normal with no focal deficit, normal cranial nerves, normal power and reflexes throughout, and no papilloedema. There are no features suggesting an intracranial mass. She is symptomatic and this is not a surveillance study. Requesting review.

Confirm:

- [ ] **TRUE** — Documented neurological sign or symptom prompting evaluation  
      *note must state this is met*
- [ ] **FALSE** — New onset headache accompanied by a focal neurological deficit  
      *note must state this is NOT met*
- [ ] **TRUE** — Headache refractory to at least 3 months of standard preventive therapy  
      *note must state this is met*
- [ ] **FALSE** — Clinical suspicion of intracranial mass with supporting examination findings  
      *note must state this is NOT met*
- [ ] **FALSE** — Study requested solely for routine surveillance in an asymptomatic patient  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C010 — Continuous positive airway pressure device (HCPCS E0601)

stratum `clear_approve` · gold **APPROVED**

> Patient: Wendell Achterberg. MRN: 6608241. DOB: 02/19/1971. Referring clinician: F. Kowalczyk, MD. Requesting HCPCS E0601, continuous positive airway pressure device with humidifier. Attended in-laboratory polysomnography was performed 14 June 2026 at this institution, within the past twelve months. The study demonstrated an apnoea hypopnoea index of 32.4 events per hour with a nadir oxygen saturation of 81 percent and significant sleep fragmentation, predominantly obstructive events in the supine position. A face to face clinical evaluation was conducted 22 July 2026 by the undersigned prior to this order, documenting an Epworth Sleepiness Scale of 17, witnessed apnoeas reported by his spouse, morning headaches, and a neck circumference of 44 cm. Titration identified an effective pressure of 11 cm H2O with a nasal pillow interface. He tolerated the interface throughout the titration study without difficulty and expressed willingness to proceed with therapy. No prior positive airway pressure trials have been attempted or abandoned. Requesting review.

Confirm:

- [ ] **TRUE** — Diagnostic sleep study completed within the previous 12 months  
      *note must state this is met*
- [ ] **TRUE** — Apnoea hypopnoea index of 15 or greater, or 5 or greater with documented symptoms or cardiovascular comorbidity  
      *note must state this is met*
- [ ] **TRUE** — Face to face clinical evaluation by the treating clinician documented prior to the order  
      *note must state this is met*
- [ ] **FALSE** — Documented inability to tolerate positive airway pressure with no alternative interface trialled  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C011 — Attended polysomnography in a sleep laboratory (CPT 95810)

stratum `borderline` · gold **APPROVED**

> Patient: Ingrid Solheim. MRN: 4402996. DOB: 07/26/1962. Referring clinician: B. Nwachukwu, MD. Requesting CPT 95810, attended polysomnography in a sleep laboratory. Patient reports habitual loud snoring nightly, witnessed apnoeic pauses described by her partner, and excessive daytime sleepiness with an Epworth Sleepiness Scale of 13, including two episodes of drowsiness while driving in the past month. Her history includes heart failure with preserved ejection fraction, diagnosed 2024, with an ejection fraction of 52 percent, NYHA class II symptoms, and a most recent NT-proBNP of 410 pg/mL. She is maintained on furosemide and sacubitril-valsartan and was last decompensated 14 months ago. This comorbid cardiac condition is present and stable but sufficient to make home sleep apnoea testing unreliable in her case, as ambulatory devices systematically underestimate the apnoea hypopnoea index in the presence of heart failure and cannot characterise central events. No home sleep study has previously been performed. Her presentation is one of sleep disordered breathing, not primary insomnia. Requesting review.

Confirm:

- [ ] **TRUE** — Documented symptoms of sleep disordered breathing such as habitual snoring, witnessed apnoea, or excessive daytime sleepiness  
      *note must state this is met*
- [ ] **TRUE** — Comorbid condition making home sleep apnoea testing unreliable, such as heart failure, chronic lung disease, or neuromuscular disease  
      *note must state this is met*
- [ ] **FALSE** — Prior home sleep apnoea test that was technically inadequate or negative despite persistent symptoms  
      *note must state this is NOT met*
- [ ] **FALSE** — Study requested solely for evaluation of insomnia without features of sleep disordered breathing  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C012 — Shoulder arthroscopy with rotator cuff repair (CPT 29827)

stratum `clear_deny` · gold **DENIED**

> Patient: Rashid Al-Mansouri. MRN: 5518703. DOB: 10/07/1979. Referring clinician: G. Petrossian, MD. Requesting CPT 29827, shoulder arthroscopy with rotator cuff repair, right shoulder. Patient sustained an acute injury on 12 May 2026 when he fell from a ladder onto the outstretched right arm, with immediate pain and loss of overhead function; he is 46 years of age. MRI of the right shoulder dated 30 May 2026 demonstrates a partial thickness articular sided tear of the supraspinatus involving approximately 40 percent of tendon thickness, with intact bursal fibres and no retraction. The tendon is not fully disrupted and no full thickness defect is identified. Conservative management has run eight weeks and included 16 supervised physical therapy sessions, a subacromial corticosteroid injection, and activity modification, without adequate symptomatic improvement. On examination today, supraspinatus strength is 5 out of 5 with a negative drop arm sign and no weakness demonstrable on empty can testing. Glenohumeral joint space is preserved with no arthritic change or cuff arthropathy. Requesting review.

Confirm:

- [ ] **FALSE** — Imaging confirmation of a full thickness rotator cuff tear  
      *note must state this is NOT met*
- [ ] **TRUE** — Failed conservative management for at least 6 weeks including physical therapy  
      *note must state this is met*
- [ ] **FALSE** — Persistent weakness on examination of the affected shoulder  
      *note must state this is NOT met*
- [ ] **TRUE** — Acute traumatic tear in a patient under 60 years of age  
      *note must state this is met*
- [ ] **FALSE** — Advanced glenohumeral arthritis or established rotator cuff arthropathy  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C013 — Lumbar spinal fusion, single level (CPT 22612)

stratum `clear_deny` · gold **DENIED**

> Patient: Frances Odunlami. MRN: 2276549. DOB: 03/03/1966. Referring clinician: H. Lindgren, MD. Requesting CPT 22612, single level lumbar fusion at L5-S1. Patient reports six years of axial low back pain with intermittent radiation to the posterior thighs. Dynamic flexion-extension radiographs dated 18 June 2026 show no translation at any lumbar level on either view, and MRI dated 21 June 2026 demonstrates disc desiccation and modest height loss at L5-S1 without spondylolisthesis, without pars defect, and with no evidence of segmental instability at the proposed operative level. Non-operative management has extended over four years and included two prolonged courses of physical therapy totalling 40 sessions, aquatic therapy, NSAIDs, duloxetine, and three epidural steroid injections. Symptoms localise to the L5-S1 distribution and correlate with the imaged level on provocative examination. She has never smoked. DEXA dated 11 April 2026 records a T-score of negative 1.4. Requesting review.

Confirm:

- [ ] **FALSE** — Radiographic confirmation of spondylolisthesis or segmental instability at the operative level  
      *note must state this is NOT met*
- [ ] **TRUE** — Failed at least 6 months of non-operative management including physical therapy  
      *note must state this is met*
- [ ] **TRUE** — Concordant symptoms correlating with the imaged level  
      *note must state this is met*
- [ ] **FALSE** — Active nicotine use without documented cessation counselling  
      *note must state this is NOT met*
- [ ] **FALSE** — Untreated osteoporosis with T-score below negative 2.5  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C014 — Attended polysomnography in a sleep laboratory (CPT 95810)  **FLAGGED**

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Emeka Balogun. MRN: 8871360. DOB: 11/18/1974. Referring clinician: C. Marchetti, MD. Requesting CPT 95810, attended polysomnography. Patient underwent a home sleep apnoea test on 03 April 2026. The study aborted after 2 hours 10 minutes of recording owing to nasal cannula displacement and loss of the oximetry signal, and the interpreting physician documented the study as technically inadequate with insufficient valid recording time to generate a scorable apnoea hypopnoea index. A repeat home study was attempted 25 April 2026 and again failed on signal quality grounds. He has hypertension on two agents and a body mass index of 34.6. Physical examination shows a Mallampati class III airway and a neck circumference of 42 cm. This referral is not for evaluation of insomnia; sleep onset and maintenance are not the presenting concern. He has no history of heart failure, chronic lung disease, or neuromuscular disease. Requesting review for attended in-laboratory study.

Confirm:

- [ ] **ABSENT** — Documented symptoms of sleep disordered breathing such as habitual snoring, witnessed apnoea, or excessive daytime sleepiness  
      *note must NOT establish this either way*
- [ ] **FALSE** — Comorbid condition making home sleep apnoea testing unreliable, such as heart failure, chronic lung disease, or neuromuscular disease  
      *note must state this is NOT met*
- [ ] **TRUE** — Prior home sleep apnoea test that was technically inadequate or negative despite persistent symptoms  
      *note must state this is met*
- [ ] **FALSE** — Study requested solely for evaluation of insomnia without features of sleep disordered breathing  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C015 — Brain MRI with contrast (CPT 70553)

stratum `clear_approve` · gold **APPROVED**

> Patient: Delphine Rousseau. MRN: 3364817. DOB: 08/22/1957. Referring clinician: A. Sundaram, MD. Requesting CPT 70553, MRI of the brain with and without contrast. Patient presents with a six week history of progressive expressive dysphasia and new onset word finding difficulty, together with two witnessed focal seizures with secondary generalisation. On examination there is mild right upper limb pronator drift, a right facial droop sparing the forehead, and hyperreflexia on the right, constituting clear neurological signs prompting evaluation. Fundoscopy demonstrates early papilloedema bilaterally. Non-contrast CT head performed 02 August 2026 in the emergency department shows a 2.8 cm left frontal region of vasogenic oedema with mild midline shift and an ill defined hypodensity, findings that raise clinical suspicion of an intracranial mass and are supported by the focal examination findings above. She has no prior headache history and no history of migraine or of preventive therapy. This is not routine surveillance and she is not asymptomatic. Requesting review.

Confirm:

- [ ] **TRUE** — Documented neurological sign or symptom prompting evaluation  
      *note must state this is met*
- [ ] **FALSE** — New onset headache accompanied by a focal neurological deficit  
      *note must state this is NOT met*
- [ ] **FALSE** — Headache refractory to at least 3 months of standard preventive therapy  
      *note must state this is NOT met*
- [ ] **TRUE** — Clinical suspicion of intracranial mass with supporting examination findings  
      *note must state this is met*
- [ ] **FALSE** — Study requested solely for routine surveillance in an asymptomatic patient  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C016 — Continuous positive airway pressure device (HCPCS E0601)

stratum `clear_deny` · gold **DENIED**

> Patient: Gustave Lemieux. MRN: 7719052. DOB: 06/14/1980. Referring clinician: M. Osei, MD. Requesting HCPCS E0601, continuous positive airway pressure device. Attended polysomnography was completed 19 March 2026, within the preceding twelve months. The study recorded an apnoea hypopnoea index of 3.1 events per hour across 6 hours 40 minutes of recorded sleep, with a nadir oxygen saturation of 93 percent and no significant desaturation events. The index therefore falls below the 5 event threshold entirely. Face to face clinical evaluation was performed by the undersigned on 28 July 2026 prior to this order, documenting the patient's reported fatigue, an Epworth Sleepiness Scale of 9, and a body mass index of 27.4. His spouse reports light snoring but no witnessed apnoeic pauses. He has no diagnosed cardiovascular comorbidity, no hypertension, no arrhythmia, and no history of stroke. He has not previously trialled positive airway pressure and no interface intolerance has been documented. Requesting review.

Confirm:

- [ ] **TRUE** — Diagnostic sleep study completed within the previous 12 months  
      *note must state this is met*
- [ ] **FALSE** — Apnoea hypopnoea index of 15 or greater, or 5 or greater with documented symptoms or cardiovascular comorbidity  
      *note must state this is NOT met*
- [ ] **TRUE** — Face to face clinical evaluation by the treating clinician documented prior to the order  
      *note must state this is met*
- [ ] **FALSE** — Documented inability to tolerate positive airway pressure with no alternative interface trialled  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C017 — Lumbar spine MRI without contrast (CPT 72148)

stratum `clear_deny` · gold **DENIED**

> Patient: Sylvia Mwangi. MRN: 4408736. DOB: 02/28/1972. Referring clinician: R. Delacroix, MD. Requesting CPT 72148, MRI of the lumbar spine without contrast. Patient reports low back pain of five months duration, unchanged in character or severity since onset. She completed a 10 week course of supervised physical therapy concluding 14 May 2026, 22 sessions in total, without adequate relief. Review of systems is notable for a 7 kg unintentional weight loss over four months and intermittent night sweats; she has no known malignancy but these constitute red flag features warranting attention. Examination shows no focal motor deficit, symmetric reflexes, and intact sensation throughout both lower limbs. Of note, MRI of the lumbar spine without contrast was performed at this institution on 08 April 2026, four months ago, demonstrating mild multilevel degenerative change without stenosis or nerve root compression. Her symptoms have not changed in distribution, severity, or character since that study, and no new neurological findings have emerged in the interval. Requesting review.

Confirm:

- [ ] **TRUE** — Low back pain documented for at least 6 weeks  
      *note must state this is met*
- [ ] **TRUE** — Completed at least 4 weeks of supervised physical therapy without adequate relief  
      *note must state this is met*
- [ ] **FALSE** — Focal neurological deficit on examination  
      *note must state this is NOT met*
- [ ] **TRUE** — Red flag features present (unexplained weight loss, fever, history of malignancy, or bowel or bladder dysfunction)  
      *note must state this is met*
- [ ] **TRUE** — Lumbar MRI of the same region performed within the previous 6 months with no interval change in symptoms  
      *note must state this is met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C018 — Total knee arthroplasty (CPT 27447)

stratum `clear_approve` · gold **APPROVED**

> Patient: Aloysius Pemberton. MRN: 3352907. DOB: 12/09/1953. Referring clinician: K. Nakamura, MD. Requesting CPT 27447, total knee arthroplasty, right knee. Standing radiographs dated 11 June 2026 demonstrate bone on bone contact in the medial compartment with complete joint space loss, large marginal osteophytes, subchondral sclerosis and cyst formation, and varus deformity, reported as Kellgren-Lawrence grade 4. Conservative management has extended over 14 months and included meloxicam, two courses of physical therapy totalling 24 sessions, three intra-articular corticosteroid injections, and a course of viscosupplementation, with progressive rather than improving symptoms. He can no longer climb the stairs to his bedroom and has relocated to a ground floor room, cannot walk to his mailbox, and has stopped driving because of difficulty transferring. He requires assistance with lower body dressing. Body mass index 31.2. Weight has been stable. No fever, no joint effusion, no overlying skin breakdown, no recent infection at any site, and normal white cell count with a CRP of 3 mg/L. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic evidence of advanced osteoarthritis (Kellgren-Lawrence grade 3 or 4)  
      *note must state this is met*
- [ ] **TRUE** — Failed conservative management for at least 3 months including NSAIDs and physical therapy  
      *note must state this is met*
- [ ] **TRUE** — Documented functional limitation affecting activities of daily living  
      *note must state this is met*
- [ ] **FALSE** — Active infection of the joint or of an adjacent surgical site  
      *note must state this is NOT met*
- [ ] **FALSE** — Body mass index of 45 or greater without documented weight management plan  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C019 — Coronary computed tomography angiography (CPT 75574)

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Marguerite Okonjo. MRN: 8846213. DOB: 05/21/1968. Referring clinician: T. Brennan, MD. Requesting CPT 75574, coronary computed tomography angiography. Patient presents with a four month history of substernal chest tightness occurring reproducibly after climbing two flights of stairs and resolving within five minutes of rest, together with exertional dyspnoea disproportionate to her baseline. The character and reproducibility of these symptoms are consistent with an anginal syndrome. Resting electrocardiogram shows normal sinus rhythm without ischaemic change. She has not previously undergone invasive coronary angiography and carries no prior diagnosis of obstructive coronary artery disease. Serum creatinine 0.8 mg/dL with an estimated glomerular filtration rate of 79 mL/min/1.73m2, and she has no contraindication to iodinated contrast. Beta blockade is in place with a resting heart rate of 61. Anatomic assessment is requested to characterise her coronary anatomy and guide management. Requesting review.

Confirm:

- [ ] **TRUE** — Symptoms suggestive of coronary artery disease such as chest pain or anginal equivalent  
      *note must state this is met*
- [ ] **ABSENT** — Low to intermediate pretest probability of obstructive coronary disease documented  
      *note must NOT establish this either way*
- [ ] **FALSE** — Known obstructive coronary artery disease already confirmed on invasive angiography  
      *note must state this is NOT met*
- [ ] **FALSE** — Estimated glomerular filtration rate below 30 without nephrology clearance  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C020 — Shoulder arthroscopy with rotator cuff repair (CPT 29827)

stratum `retrieval_distractor` · gold **APPROVED**

> Patient: Bartholomew Ngata. MRN: 2264891. DOB: 09/03/1979. Referring clinician: E. Villanueva, MD. Requesting CPT 29827, arthroscopic rotator cuff repair, left shoulder. Patient is 46 years old and sustained an acute injury on 04 April 2026 when a loaded pallet struck his outstretched left arm at work, with immediate sharp pain and inability to lift the arm above shoulder height. MRI dated 18 April 2026 demonstrates a full thickness tear of the supraspinatus tendon measuring 1.9 cm in anteroposterior dimension with 8 mm of medial retraction and fluid tracking into the subacromial bursa. Conservative management has run 15 weeks and included 20 supervised physical therapy sessions, a subacromial injection, and NSAIDs, without functional recovery. On examination supraspinatus strength is 5 out of 5 against resistance with a negative drop arm sign and no demonstrable weakness. Glenohumeral joint spaces are preserved with no arthritic change and no proximal humeral migration. Separately, he uses a CPAP device nightly for previously diagnosed sleep apnoea, unrelated to this request. Requesting review.

Confirm:

- [ ] **TRUE** — Imaging confirmation of a full thickness rotator cuff tear  
      *note must state this is met*
- [ ] **TRUE** — Failed conservative management for at least 6 weeks including physical therapy  
      *note must state this is met*
- [ ] **FALSE** — Persistent weakness on examination of the affected shoulder  
      *note must state this is NOT met*
- [ ] **TRUE** — Acute traumatic tear in a patient under 60 years of age  
      *note must state this is met*
- [ ] **FALSE** — Advanced glenohumeral arthritis or established rotator cuff arthropathy  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

- [ ] mentions a second unrelated procedure (Continuous positive airway pressure device) that does not affect the criteria

---

## C021 — Group 2 power wheelchair (HCPCS K0823)

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Constance Ferreira. MRN: 6635420. DOB: 07/12/1944. Referring clinician: P. Achterberg, MD. Requesting HCPCS K0823, Group 2 power wheelchair. Patient has post-polio syndrome with severe bilateral lower extremity weakness and progressive fatigue. She cannot ambulate from her bed to her bathroom without a rest period and is unable to complete toileting, bathing, or meal preparation within the home independently; her mobility limitation directly prevents these activities of daily living. Physical therapy specialty mobility evaluation was completed 02 April 2026 by L. Steinmetz, PT, DPT, within the past six months, documenting a gait speed of 0.31 m/s and inability to sustain ambulation beyond 4 metres. A manual wheelchair was trialled for six weeks; her upper extremity strength is graded 3 out of 5 bilaterally and she could not propel the chair over carpet or any incline, so it does not meet her needs. Her home has level access throughout and 34 inch doorways, and accommodates the device without modification. Requesting review.

Confirm:

- [ ] **TRUE** — Mobility limitation preventing completion of activities of daily living within the home  
      *note must state this is met*
- [ ] **TRUE** — Specialty evaluation by a licensed therapist completed within the previous 6 months  
      *note must state this is met*
- [ ] **ABSENT** — Patient demonstrates capacity to operate the device safely, or a caregiver is available to operate it  
      *note must NOT establish this either way*
- [ ] **FALSE** — A manual wheelchair or lesser mobility device adequately meets the patient's needs  
      *note must state this is NOT met*
- [ ] **FALSE** — Home environment cannot accommodate the device and no modification is planned  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C022 — Total hip arthroplasty (CPT 27130)

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Ignatius Oyelowo. MRN: 5573148. DOB: 04/06/1958. Referring clinician: D. Karlsson, MD. Requesting CPT 27130, total hip arthroplasty, left hip. Patient reports 18 months of progressive left groin pain with radiation to the anterior thigh. Conservative management has extended over seven months and included naproxen, 18 supervised physical therapy sessions, a fluoroscopically guided intra-articular injection, and a cane, without durable benefit. He reports pain that halts him after approximately 30 metres and he is unable to walk the length of his street. He sleeps without interruption from hip pain and denies nocturnal symptoms. Examination shows internal rotation limited to 5 degrees with pain at end range and a positive FABER test. There is no fever, no erythema, no wound, and no evidence of local or systemic infection; CRP is 2 mg/L and white cell count is normal. Requesting review for surgical planning.

Confirm:

- [ ] **ABSENT** — Radiographic evidence of advanced hip osteoarthritis, avascular necrosis, or displaced femoral neck fracture  
      *note must NOT establish this either way*
- [ ] **TRUE** — Failed conservative management for at least 3 months, or an acute fracture indication making conservative management inappropriate  
      *note must state this is met*
- [ ] **TRUE** — Pain limiting ambulation to less than one block  
      *note must state this is met*
- [ ] **FALSE** — Night pain disturbing sleep on most nights  
      *note must state this is NOT met*
- [ ] **FALSE** — Active local or systemic infection  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C023 — Hyperbaric oxygen therapy for diabetic foot ulcer (HCPCS G0277)

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Rosalind Ekwueme. MRN: 9927035. DOB: 10/29/1961. Referring clinician: A. Lindholm, MD. Requesting HCPCS G0277, hyperbaric oxygen therapy for a chronic diabetic foot ulcer. Patient has type 2 diabetes of 22 years duration with peripheral neuropathy. Ulcer over the left heel, present since December 2025, measures 4.2 by 3.6 cm and probes to bone with exposed calcaneal cortex and surrounding cellulitis; it is documented as Wagner grade 3. Standard wound care has been delivered continuously for 11 weeks, from 20 May 2026 to the present, comprising weekly sharp debridement, a removable cast walker for offloading, alginate dressings changed three times weekly, and a completed course of oral antibiotics. Wound surface area has reduced by less than 10 percent over that period and the wound is considered non-responsive to standard therapy. Chest radiograph on 01 August 2026 shows clear lung fields with no pneumothorax. Haemoglobin A1c 7.8 percent. Requesting review.

Confirm:

- [ ] **TRUE** — Wagner grade 3 or higher diabetic foot ulcer documented  
      *note must state this is met*
- [ ] **TRUE** — Failed at least 30 days of standard wound care including debridement and offloading  
      *note must state this is met*
- [ ] **ABSENT** — Adequate lower extremity perfusion confirmed by vascular assessment  
      *note must NOT establish this either way*
- [ ] **FALSE** — Untreated pneumothorax  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C024 — Roux-en-Y gastric bypass (CPT 43644)

stratum `clear_deny` · gold **DENIED**

> Patient: Anneliese Brandtner. MRN: 3319674. DOB: 08/17/1988. Referring clinician: J. Mutombo, MD. Requesting CPT 43644, laparoscopic Roux-en-Y gastric bypass. Patient weighs 91 kg at a height of 1.65 m, giving a calculated body mass index of 33.4. She carries a diagnosis of type 2 diabetes managed on metformin with a haemoglobin A1c of 7.2 percent. She completed a medically supervised weight management programme from 14 August 2025 through 20 February 2026, six consecutive months, attending 23 of 24 scheduled dietitian and exercise physiology appointments, and lost 6 kg over that period before plateauing. Preoperative psychological evaluation was completed 12 June 2026 by S. Adeoye, PsyD, documenting appropriate motivation, no active eating disorder, and clearance to proceed. She reports no alcohol, tobacco, or recreational substance use, confirmed by negative toxicology screen. She is not pregnant, uses a long acting reversible contraceptive, and has no plans to conceive. Requesting review.

Confirm:

- [ ] **FALSE** — Body mass index of 40 or greater, or 35 or greater with an obesity related comorbidity  
      *note must state this is NOT met*
- [ ] **TRUE** — Documented participation in a supervised weight management programme for at least 6 consecutive months  
      *note must state this is met*
- [ ] **TRUE** — Preoperative psychological evaluation completed and clearance documented  
      *note must state this is met*
- [ ] **FALSE** — Untreated substance use disorder  
      *note must state this is NOT met*
- [ ] **FALSE** — Pregnancy, current or planned within 12 months  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C025 — Lumbar spine MRI without contrast (CPT 72148)

stratum `clear_deny` · gold **DENIED**

> Patient: Fitzgerald Amankwah. MRN: 7784206. DOB: 01/15/1965. Referring clinician: V. Sorenson, MD. Requesting CPT 72148, MRI of the lumbar spine without contrast. Patient reports low back pain of 11 weeks duration following no identified precipitant, persistent and gradually worsening. He has a documented history of prostate adenocarcinoma treated with radical prostatectomy in 2021, and his most recent PSA drawn 24 July 2026 has risen to 4.8 ng/mL from an undetectable nadir, a red flag feature in this setting. Physical therapy was offered at the initial visit on 02 June 2026; he attended a single assessment appointment and declined to proceed with the course, and no supervised therapy has been undertaken since. Examination demonstrates full power throughout both lower limbs, symmetric and normal reflexes, and no sensory deficit; there is no focal neurological abnormality. He reports no bowel or bladder dysfunction. No previous lumbar spine imaging has been performed. Requesting review.

Confirm:

- [ ] **TRUE** — Low back pain documented for at least 6 weeks  
      *note must state this is met*
- [ ] **FALSE** — Completed at least 4 weeks of supervised physical therapy without adequate relief  
      *note must state this is NOT met*
- [ ] **FALSE** — Focal neurological deficit on examination  
      *note must state this is NOT met*
- [ ] **TRUE** — Red flag features present (unexplained weight loss, fever, history of malignancy, or bowel or bladder dysfunction)  
      *note must state this is met*
- [ ] **FALSE** — Lumbar MRI of the same region performed within the previous 6 months with no interval change in symptoms  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C026 — Total hip arthroplasty (CPT 27130)  **FLAGGED**

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Ottoline Vasquez-Reid. MRN: 4462851. DOB: 03/24/1955. Referring clinician: H. Ngozi, MD. Requesting CPT 27130, total hip arthroplasty, right hip. Radiographs dated 09 July 2026 demonstrate advanced right hip osteoarthritis with superior joint space obliteration, subchondral sclerosis, and osteophyte formation at the acetabular rim. Regarding prior treatment, she reports having seen a physiotherapist at some point in the past but the duration, number of sessions, and dates could not be established at today's visit, and no records from that episode are available to this practice. She takes paracetamol as needed. She describes pain that wakes her from sleep on four to five nights each week, requiring repositioning and often analgesia before she can settle. She continues to walk to the shops approximately 400 metres away, with rest stops but without a stopping point imposed by pain. No fever, no erythema, no evidence of infection. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic evidence of advanced hip osteoarthritis, avascular necrosis, or displaced femoral neck fracture  
      *note must state this is met*
- [ ] **ABSENT** — Failed conservative management for at least 3 months, or an acute fracture indication making conservative management inappropriate  
      *note must NOT establish this either way*
- [ ] **FALSE** — Pain limiting ambulation to less than one block  
      *note must state this is NOT met*
- [ ] **TRUE** — Night pain disturbing sleep on most nights  
      *note must state this is met*
- [ ] **FALSE** — Active local or systemic infection  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C027 — Lumbar spinal fusion, single level (CPT 22612)  **FLAGGED**

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Casimir Wojciechowski. MRN: 8873490. DOB: 11/30/1970. Referring clinician: F. Adeleke, MD. Requesting CPT 22612, single level lumbar fusion at L4-L5. Standing flexion-extension radiographs dated 26 June 2026 demonstrate grade 2 isthmic spondylolisthesis at L4-L5 with bilateral pars defects and 9 mm of anterolisthesis increasing to 12 mm on flexion, confirming segmental instability at the operative level. His presenting symptoms are neurogenic claudication with bilateral L5 distribution radicular pain and a positive femoral stretch test, concordant with the level demonstrated on imaging and correlating on selective nerve root block. Regarding non-operative treatment, the record documents that management has been undertaken over an unspecified period at an outside facility; the duration, modalities, and dates of any physical therapy course are not available in the notes provided and could not be established today. He has never smoked. DEXA dated 03 March 2026 records a T-score of negative 1.1. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic confirmation of spondylolisthesis or segmental instability at the operative level  
      *note must state this is met*
- [ ] **ABSENT** — Failed at least 6 months of non-operative management including physical therapy  
      *note must NOT establish this either way*
- [ ] **TRUE** — Concordant symptoms correlating with the imaged level  
      *note must state this is met*
- [ ] **FALSE** — Active nicotine use without documented cessation counselling  
      *note must state this is NOT met*
- [ ] **FALSE** — Untreated osteoporosis with T-score below negative 2.5  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C028 — Hyperbaric oxygen therapy for diabetic foot ulcer (HCPCS G0277)

stratum `clear_deny` · gold **DENIED**

> Patient: Emmanuelle Bergstrom. MRN: 2237185. DOB: 06/02/1947. Referring clinician: L. Chukwu, MD. Requesting HCPCS G0277, hyperbaric oxygen therapy for a diabetic foot ulcer. Patient has type 1 diabetes of 41 years duration. Ulcer over the right lateral fifth metatarsal head, present since January 2026, measures 2.8 by 2.2 cm with deep probing to tendon and joint capsule, documented as Wagner grade 3. Standard wound care has been delivered for 16 weeks including six debridements, offloading with a total contact cast, and negative pressure wound therapy, without measurable closure. Vascular assessment on 04 August 2026 documents an ankle brachial index of 0.38 on the right with monophasic waveforms, absent dorsalis pedis and posterior tibial pulses on Doppler, and periwound transcutaneous oximetry of 18 mmHg. Perfusion at the wound bed is insufficient to support healing and vascular surgery review for possible revascularisation is pending. Chest radiograph clear with no pneumothorax. Requesting review.

Confirm:

- [ ] **TRUE** — Wagner grade 3 or higher diabetic foot ulcer documented  
      *note must state this is met*
- [ ] **TRUE** — Failed at least 30 days of standard wound care including debridement and offloading  
      *note must state this is met*
- [ ] **FALSE** — Adequate lower extremity perfusion confirmed by vascular assessment  
      *note must state this is NOT met*
- [ ] **FALSE** — Untreated pneumothorax  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C029 — Brain MRI with contrast (CPT 70553)

stratum `retrieval_distractor` · gold **APPROVED**

> Patient: Leopoldine Achebe. MRN: 6690523. DOB: 02/08/1969. Referring clinician: G. Ranganathan, MD. Requesting CPT 70553, MRI of the brain with and without contrast. Patient presents with eight weeks of progressive right sided hemiparesis and new onset seizure activity, with two generalised tonic-clonic events witnessed in the past three weeks. Neurological examination documents 4 out of 5 power in the right upper and lower limbs, an extensor plantar response on the right, and mild expressive dysphasia, constituting definite neurological signs. Non-contrast CT head performed 29 July 2026 shows a 3.4 cm heterogeneous left parietal lesion with surrounding vasogenic oedema and 4 mm of midline shift, raising clinical suspicion of an intracranial mass supported by the corresponding focal findings on examination. She has no history of migraine, no history of preventive headache therapy, and her headache is of recent onset without aura. She is symptomatic and this is not a surveillance study. Separately, she is on the waiting list for an elective right knee replacement for osteoarthritis, unrelated to this request. Requesting review.

Confirm:

- [ ] **TRUE** — Documented neurological sign or symptom prompting evaluation  
      *note must state this is met*
- [ ] **FALSE** — New onset headache accompanied by a focal neurological deficit  
      *note must state this is NOT met*
- [ ] **FALSE** — Headache refractory to at least 3 months of standard preventive therapy  
      *note must state this is NOT met*
- [ ] **TRUE** — Clinical suspicion of intracranial mass with supporting examination findings  
      *note must state this is met*
- [ ] **FALSE** — Study requested solely for routine surveillance in an asymptomatic patient  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

- [ ] mentions a second unrelated procedure (Total knee arthroplasty) that does not affect the criteria

---

## C030 — Roux-en-Y gastric bypass (CPT 43644)

stratum `clear_approve` · gold **APPROVED**

> Patient: Thaddeus Oyelaran. MRN: 5528967. DOB: 12/17/1982. Referring clinician: R. Kaufmann, MD. Requesting CPT 43644, laparoscopic Roux-en-Y gastric bypass. Patient weighs 138 kg at a height of 1.78 m, giving a calculated body mass index of 43.6, which exceeds the 40 threshold independent of comorbidity. He additionally carries diagnoses of obstructive sleep apnoea on CPAP and hypertension on three agents. He completed a medically supervised weight management programme at this centre from 06 October 2025 through 09 April 2026, six consecutive months, with fortnightly dietitian contact, supervised exercise sessions, and documented attendance at 25 of 26 appointments. Preoperative psychological evaluation was performed 27 May 2026 by N. Vasilenko, PsyD, who documented adequate insight, no untreated psychiatric illness, and formal clearance for surgery. He reports no alcohol intake, has never used tobacco, and denies recreational substance use, with a negative screen on 27 May 2026. He is male and pregnancy is not applicable. Requesting review.

Confirm:

- [ ] **TRUE** — Body mass index of 40 or greater, or 35 or greater with an obesity related comorbidity  
      *note must state this is met*
- [ ] **TRUE** — Documented participation in a supervised weight management programme for at least 6 consecutive months  
      *note must state this is met*
- [ ] **TRUE** — Preoperative psychological evaluation completed and clearance documented  
      *note must state this is met*
- [ ] **FALSE** — Untreated substance use disorder  
      *note must state this is NOT met*
- [ ] **FALSE** — Pregnancy, current or planned within 12 months  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C031 — Group 2 power wheelchair (HCPCS K0823)  **FLAGGED**

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Ambrose Fitzwilliam. MRN: 7745039. DOB: 05/19/1948. Referring clinician: M. Delacroix, MD. Requesting HCPCS K0823, Group 2 power wheelchair. Patient has advanced Parkinson disease with marked bradykinesia and freezing of gait. He is unable to cross his living room to reach the kitchen without freezing episodes requiring assistance, and cannot independently complete meal preparation, toileting, or dressing within the home; the mobility limitation is the direct barrier to these activities. Occupational therapy specialty mobility evaluation was completed 28 May 2026 by T. Abubakar, OTR/L, within the past six months. A manual wheelchair and a rolling walker were both trialled over ten weeks; rigidity and impaired grip strength prevented effective self-propulsion and the walker precipitated forward festination, so neither meets his needs. Regarding operation of a powered device, a driving assessment was scheduled for 11 June 2026 but the patient did not attend and it has not been rescheduled; no caregiver availability has been recorded in the chart. Home assessment confirms level access and adequate turning radius throughout. Requesting review.

Confirm:

- [ ] **TRUE** — Mobility limitation preventing completion of activities of daily living within the home  
      *note must state this is met*
- [ ] **TRUE** — Specialty evaluation by a licensed therapist completed within the previous 6 months  
      *note must state this is met*
- [ ] **ABSENT** — Patient demonstrates capacity to operate the device safely, or a caregiver is available to operate it  
      *note must NOT establish this either way*
- [ ] **FALSE** — A manual wheelchair or lesser mobility device adequately meets the patient's needs  
      *note must state this is NOT met*
- [ ] **FALSE** — Home environment cannot accommodate the device and no modification is planned  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C032 — Total knee arthroplasty (CPT 27447)  **FLAGGED**

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Wilhelmina Osei-Bonsu. MRN: 3396712. DOB: 09/08/1956. Referring clinician: D. Ferreira, MD. Requesting CPT 27447, total knee arthroplasty, left knee. Weight-bearing radiographs dated 17 July 2026 demonstrate marked medial compartment joint space loss with bone on bone apposition, large osteophytes, and subchondral sclerosis, reported as Kellgren-Lawrence grade 4. Regarding prior conservative treatment, she reports having tried anti-inflammatory medication and some exercises but is unable to specify durations or dates, no supervised physical therapy records are available from any provider, and the chart contains no documentation of the modalities attempted or the period over which they were delivered. She reports she can no longer stand long enough to cook a meal, has given up her weekly church attendance because of the walk from the car park, and requires a handrail and one assisting arm to manage the four steps at her front door. Body mass index 29.8. No fever, effusion, erythema, or recent infection at any site. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic evidence of advanced osteoarthritis (Kellgren-Lawrence grade 3 or 4)  
      *note must state this is met*
- [ ] **ABSENT** — Failed conservative management for at least 3 months including NSAIDs and physical therapy  
      *note must NOT establish this either way*
- [ ] **TRUE** — Documented functional limitation affecting activities of daily living  
      *note must state this is met*
- [ ] **FALSE** — Active infection of the joint or of an adjacent surgical site  
      *note must state this is NOT met*
- [ ] **FALSE** — Body mass index of 45 or greater without documented weight management plan  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C033 — Coronary computed tomography angiography (CPT 75574)

stratum `clear_approve` · gold **APPROVED**

> Patient: Cornelius Ravensworth. MRN: 8817244. DOB: 03/11/1966. Referring clinician: A. Nkemelu, MD. Requesting CPT 75574, coronary computed tomography angiography. Patient reports a ten week history of exertional chest pressure radiating to the left jaw, occurring reliably at a fixed workload of approximately two flights of stairs and relieved by rest within three to four minutes, an anginal presentation. Risk factors comprise treated hypertension and a total cholesterol of 214 mg/dL; he has never smoked and there is no family history of premature coronary disease. Using the pooled cohort equations together with symptom character, age, and sex, his pretest probability of obstructive coronary artery disease is documented at 21 percent, falling within the low to intermediate band. He has never undergone invasive coronary angiography and has no established diagnosis of obstructive coronary disease. Serum creatinine 1.0 mg/dL with an estimated glomerular filtration rate of 82 mL/min/1.73m2. Resting heart rate 56 on bisoprolol. Requesting review.

Confirm:

- [ ] **TRUE** — Symptoms suggestive of coronary artery disease such as chest pain or anginal equivalent  
      *note must state this is met*
- [ ] **TRUE** — Low to intermediate pretest probability of obstructive coronary disease documented  
      *note must state this is met*
- [ ] **FALSE** — Known obstructive coronary artery disease already confirmed on invasive angiography  
      *note must state this is NOT met*
- [ ] **FALSE** — Estimated glomerular filtration rate below 30 without nephrology clearance  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C034 — Continuous positive airway pressure device (HCPCS E0601)

stratum `borderline` · gold **APPROVED**

> Patient: Genevieve Sandoval-Ekwe. MRN: 4478156. DOB: 07/04/1975. Referring clinician: P. Lindqvist, MD. Requesting HCPCS E0601, continuous positive airway pressure device. Home sleep apnoea testing was completed 21 August 2025, eleven months and nineteen days prior to this order and therefore within the preceding twelve months. The study recorded an apnoea hypopnoea index of exactly 15.0 events per hour over 7 hours 12 minutes of valid recording, with a nadir saturation of 86 percent and predominantly obstructive events. Face to face clinical evaluation was carried out by the undersigned on 04 August 2026 in advance of this order, documenting an Epworth Sleepiness Scale of 12, witnessed apnoeas reported by her partner, morning dry mouth, and a body mass index of 31.9. An autotitrating device is proposed with a nasal mask interface. She has not previously used positive airway pressure and no intolerance or interface failure has been recorded. Requesting review.

Confirm:

- [ ] **TRUE** — Diagnostic sleep study completed within the previous 12 months  
      *note must state this is met*
- [ ] **TRUE** — Apnoea hypopnoea index of 15 or greater, or 5 or greater with documented symptoms or cardiovascular comorbidity  
      *note must state this is met*
- [ ] **TRUE** — Face to face clinical evaluation by the treating clinician documented prior to the order  
      *note must state this is met*
- [ ] **FALSE** — Documented inability to tolerate positive airway pressure with no alternative interface trialled  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C035 — Attended polysomnography in a sleep laboratory (CPT 95810)

stratum `clear_deny` · gold **DENIED**

> Patient: Reginald Achterhof. MRN: 2295803. DOB: 04/27/1959. Referring clinician: S. Onwuachi, MD. Requesting CPT 95810, attended polysomnography in a sleep laboratory. Patient presents with a nine month history of difficulty initiating sleep, typically lying awake for 90 to 120 minutes after retiring, together with early morning wakening at approximately 4 am and inability to return to sleep. He describes rumination and clock watching at night. His partner reports that he lies still and quiet through the night; there is no snoring, no gasping, no choking, and no witnessed pause in breathing at any time. He denies daytime sleepiness, with an Epworth Sleepiness Scale of 4, and reports fatigue rather than somnolence. Body mass index 23.1, neck circumference 36 cm, Mallampati class I. He has had a previous home sleep apnoea test in 2023 which was technically adequate and recorded an apnoea hypopnoea index of 1.8. He has no heart failure, chronic lung disease, or neuromuscular disease. Requesting review.

Confirm:

- [ ] **FALSE** — Documented symptoms of sleep disordered breathing such as habitual snoring, witnessed apnoea, or excessive daytime sleepiness  
      *note must state this is NOT met*
- [ ] **FALSE** — Comorbid condition making home sleep apnoea testing unreliable, such as heart failure, chronic lung disease, or neuromuscular disease  
      *note must state this is NOT met*
- [ ] **TRUE** — Prior home sleep apnoea test that was technically inadequate or negative despite persistent symptoms  
      *note must state this is met*
- [ ] **FALSE** — Study requested solely for evaluation of insomnia without features of sleep disordered breathing  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C036 — Shoulder arthroscopy with rotator cuff repair (CPT 29827)

stratum `clear_deny` · gold **DENIED**

> Patient: Marcelline Duvivier. MRN: 6653928. DOB: 08/09/1951. Referring clinician: K. Balogun, MD. Requesting CPT 29827, arthroscopic rotator cuff repair, right shoulder. MRI dated 12 June 2026 demonstrates a full thickness tear of the supraspinatus with 2.4 cm of retraction and associated infraspinatus involvement. The same study reports superior migration of the humeral head with an acromiohumeral interval of 4 mm, Hamada grade 3 change, moderate glenohumeral joint space narrowing with subchondral sclerosis and inferior humeral osteophyte formation, and Goutallier grade 3 fatty infiltration of the cuff musculature, consistent with established rotator cuff arthropathy and advanced glenohumeral arthritis. Conservative management has run 14 weeks with 19 physical therapy sessions and two subacromial injections without benefit. Examination shows 3 out of 5 strength on empty can testing with a positive drop arm sign, indicating persistent weakness. She is 74 years old and reports insidious onset over two years without any traumatic event. Requesting review.

Confirm:

- [ ] **TRUE** — Imaging confirmation of a full thickness rotator cuff tear  
      *note must state this is met*
- [ ] **TRUE** — Failed conservative management for at least 6 weeks including physical therapy  
      *note must state this is met*
- [ ] **TRUE** — Persistent weakness on examination of the affected shoulder  
      *note must state this is met*
- [ ] **FALSE** — Acute traumatic tear in a patient under 60 years of age  
      *note must state this is NOT met*
- [ ] **TRUE** — Advanced glenohumeral arthritis or established rotator cuff arthropathy  
      *note must state this is met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C037 — Continuous positive airway pressure device (HCPCS E0601)

stratum `clear_deny` · gold **DENIED**

> Patient: Barnabas Whitlock. MRN: 9938471. DOB: 01/22/1984. Referring clinician: E. Mkhize, MD. Requesting HCPCS E0601, continuous positive airway pressure device. Patient carries a diagnosis of obstructive sleep apnoea made on attended polysomnography performed 14 February 2023, three years and six months prior to this order; no sleep study has been undertaken within the preceding twelve months and no repeat testing is scheduled. That historical study recorded an apnoea hypopnoea index of 28.6 events per hour with a nadir saturation of 84 percent. Face to face clinical evaluation was performed by the undersigned on 30 July 2026 in advance of this order, documenting continued snoring, witnessed apnoeas, an Epworth Sleepiness Scale of 14, and a body mass index of 36.1. He previously owned a device which was lost during a house move in 2024 and he has been untreated since. He tolerated therapy well during the period he used it and reports no interface difficulty. Requesting review.

Confirm:

- [ ] **FALSE** — Diagnostic sleep study completed within the previous 12 months  
      *note must state this is NOT met*
- [ ] **TRUE** — Apnoea hypopnoea index of 15 or greater, or 5 or greater with documented symptoms or cardiovascular comorbidity  
      *note must state this is met*
- [ ] **TRUE** — Face to face clinical evaluation by the treating clinician documented prior to the order  
      *note must state this is met*
- [ ] **FALSE** — Documented inability to tolerate positive airway pressure with no alternative interface trialled  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C038 — Shoulder arthroscopy with rotator cuff repair (CPT 29827)  **FLAGGED**

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Perpetua Nwosu-Hartley. MRN: 5561290. DOB: 06/16/1972. Referring clinician: J. Castellano, MD. Requesting CPT 29827, arthroscopic rotator cuff repair, left shoulder. Patient reports six months of left shoulder pain with progressive loss of overhead reach following a fall in February 2026. Conservative management has run 19 weeks and included 24 supervised physical therapy sessions, two subacromial corticosteroid injections, and a graded home programme, without functional gain. On examination there is 3 out of 5 strength on empty can testing with a positive external rotation lag sign and a positive drop arm sign, demonstrating persistent weakness of the affected shoulder. Regarding imaging, the patient reports that an MRI was arranged by an outside provider earlier this year, but no report or images have been received by this practice despite two requests, and the findings, including whether any tear was identified and its thickness, could not be established today. Glenohumeral joint spaces appear preserved on plain radiographs with no arthritic change or cuff arthropathy. Requesting review.

Confirm:

- [ ] **ABSENT** — Imaging confirmation of a full thickness rotator cuff tear  
      *note must NOT establish this either way*
- [ ] **TRUE** — Failed conservative management for at least 6 weeks including physical therapy  
      *note must state this is met*
- [ ] **TRUE** — Persistent weakness on examination of the affected shoulder  
      *note must state this is met*
- [ ] **FALSE** — Acute traumatic tear in a patient under 60 years of age  
      *note must state this is NOT met*
- [ ] **FALSE** — Advanced glenohumeral arthritis or established rotator cuff arthropathy  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C039 — Lumbar spinal fusion, single level (CPT 22612)

stratum `clear_approve` · gold **APPROVED**

> Patient: Octavius Bramwell. MRN: 3374915. DOB: 10/03/1963. Referring clinician: N. Adisa, MD. Requesting CPT 22612, single level lumbar fusion at L5-S1. Flexion-extension radiographs dated 05 May 2026 demonstrate grade 2 degenerative spondylolisthesis at L5-S1 with 11 mm of anterolisthesis and 6 mm of dynamic translation between views, confirming segmental instability at the operative level. Non-operative management has extended over 22 months and comprised three separate courses of supervised physical therapy totalling 46 sessions, a structured spinal stabilisation programme, NSAIDs, gabapentin, duloxetine, and four epidural steroid injections, with no durable improvement. His symptoms are neurogenic claudication limiting standing tolerance to four minutes, with bilateral S1 distribution radicular pain, a diminished right Achilles reflex, and reproduction of his exact symptoms on selective S1 nerve root block, concordant with the L5-S1 level demonstrated on imaging. He has never used tobacco in any form. DEXA dated 18 February 2026 records a lowest T-score of negative 1.6. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic confirmation of spondylolisthesis or segmental instability at the operative level  
      *note must state this is met*
- [ ] **TRUE** — Failed at least 6 months of non-operative management including physical therapy  
      *note must state this is met*
- [ ] **TRUE** — Concordant symptoms correlating with the imaged level  
      *note must state this is met*
- [ ] **FALSE** — Active nicotine use without documented cessation counselling  
      *note must state this is NOT met*
- [ ] **FALSE** — Untreated osteoporosis with T-score below negative 2.5  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C040 — Total hip arthroplasty (CPT 27130)

stratum `clear_approve` · gold **APPROVED**

> Patient: Hyacinth Oduya-Merrick. MRN: 8829647. DOB: 02/14/1950. Referring clinician: R. Thibodeaux, MD. Requesting CPT 27130, total hip arthroplasty, left hip. AP pelvis radiographs dated 22 June 2026 demonstrate advanced left hip osteoarthritis with complete superolateral joint space loss, extensive subchondral sclerosis and cyst formation, and circumferential osteophytosis. Conservative management has extended over 11 months and included paracetamol, meloxicam, 26 supervised physical therapy sessions across two courses, an intra-articular corticosteroid injection, and progression from a cane to a rollator, with continued deterioration. She reports that pain now stops her within approximately 40 metres, less than one block, and she can no longer walk to the bus stop at the end of her road. She sleeps through the night without waking from hip pain. Examination shows fixed flexion of 15 degrees and internal rotation limited to 0 degrees. No fever, no erythema, no wound, no recent dental or urinary infection; CRP 2 mg/L, white cell count normal. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic evidence of advanced hip osteoarthritis, avascular necrosis, or displaced femoral neck fracture  
      *note must state this is met*
- [ ] **TRUE** — Failed conservative management for at least 3 months, or an acute fracture indication making conservative management inappropriate  
      *note must state this is met*
- [ ] **TRUE** — Pain limiting ambulation to less than one block  
      *note must state this is met*
- [ ] **FALSE** — Night pain disturbing sleep on most nights  
      *note must state this is NOT met*
- [ ] **FALSE** — Active local or systemic infection  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C041 — Group 2 power wheelchair (HCPCS K0823)

stratum `borderline` · gold **APPROVED**

> Patient: Ferdinand Achinike. MRN: 4416802. DOB: 11/07/1946. Referring clinician: A. Sorensen, MD. Requesting HCPCS K0823, Group 2 power wheelchair. Patient has amyotrophic lateral sclerosis with predominantly lower limb onset. He is unable to walk from his bedroom to his bathroom, a distance of six metres, without a rest and now requires assistance for toileting and bathing within the home; the mobility limitation directly prevents completion of these activities. Physical therapy specialty mobility evaluation was completed exactly six months ago on 09 February 2026 by C. Nwabueze, PT, DPT, documenting a manual muscle test of 2 out of 5 in both hip flexors and a six minute walk distance of 21 metres with a rollator. A manual wheelchair was trialled for eight weeks; upper limb involvement has progressed to 3 out of 5 shoulder abduction and he could not self-propel over any distance, so it does not meet his needs. He operated a demonstration power chair with accurate joystick control and safe stopping, and his wife is available as a secondary operator. The residence has level access and 36 inch doorways throughout. Requesting review.

Confirm:

- [ ] **TRUE** — Mobility limitation preventing completion of activities of daily living within the home  
      *note must state this is met*
- [ ] **TRUE** — Specialty evaluation by a licensed therapist completed within the previous 6 months  
      *note must state this is met*
- [ ] **TRUE** — Patient demonstrates capacity to operate the device safely, or a caregiver is available to operate it  
      *note must state this is met*
- [ ] **FALSE** — A manual wheelchair or lesser mobility device adequately meets the patient's needs  
      *note must state this is NOT met*
- [ ] **FALSE** — Home environment cannot accommodate the device and no modification is planned  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C042 — Coronary computed tomography angiography (CPT 75574)

stratum `clear_deny` · gold **DENIED**

> Patient: Seraphina Kowalczyk-Obi. MRN: 6674531. DOB: 05/25/1954. Referring clinician: T. Amaechi, MD. Requesting CPT 75574, coronary computed tomography angiography. Patient reports intermittent chest discomfort described as a heavy ache across the anterior chest, present at rest and at exertion without a clear relationship to activity, over the past five months, together with dyspnoea on climbing stairs. Risk factors include type 2 diabetes of 16 years duration with a haemoglobin A1c of 8.4 percent, hypertension on three agents, hyperlipidaemia with an LDL of 156 mg/dL, a 30 pack year smoking history with ongoing daily use, peripheral arterial disease with an ankle brachial index of 0.72, and a father who died of myocardial infarction at 51. Applying the pooled cohort equations with this risk profile and her symptom character, documented pretest probability of obstructive coronary artery disease is 76 percent, a high pretest likelihood. She has not previously undergone invasive coronary angiography. Estimated glomerular filtration rate 68 mL/min/1.73m2. Requesting review.

Confirm:

- [ ] **TRUE** — Symptoms suggestive of coronary artery disease such as chest pain or anginal equivalent  
      *note must state this is met*
- [ ] **FALSE** — Low to intermediate pretest probability of obstructive coronary disease documented  
      *note must state this is NOT met*
- [ ] **FALSE** — Known obstructive coronary artery disease already confirmed on invasive angiography  
      *note must state this is NOT met*
- [ ] **FALSE** — Estimated glomerular filtration rate below 30 without nephrology clearance  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C043 — Total knee arthroplasty (CPT 27447)

stratum `clear_approve` · gold **APPROVED**

> Patient: Lucretia Vandermeer. MRN: 2248379. DOB: 12/30/1957. Referring clinician: H. Okwuosa, MD. Requesting CPT 27447, total knee arthroplasty, right knee. Standing radiographs dated 30 June 2026 demonstrate complete lateral compartment joint space obliteration with bone on bone contact, extensive osteophytosis, subchondral sclerosis and cyst formation, and valgus malalignment, reported as Kellgren-Lawrence grade 4. Conservative management has extended over 19 months and included celecoxib, two courses of supervised physical therapy totalling 30 sessions, two intra-articular corticosteroid injections, a knee brace, and a course of viscosupplementation, with progressive worsening throughout. She is unable to rise from a standard chair without pushing up on both arms, has stopped using her upstairs bathroom, cannot walk the 200 metres to her daughter's house, and now requires help with putting on shoes and socks. Body mass index 33.7 and stable. No fever, no effusion, no warmth or erythema, no skin breakdown, no recent infection at any site; CRP 4 mg/L. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic evidence of advanced osteoarthritis (Kellgren-Lawrence grade 3 or 4)  
      *note must state this is met*
- [ ] **TRUE** — Failed conservative management for at least 3 months including NSAIDs and physical therapy  
      *note must state this is met*
- [ ] **TRUE** — Documented functional limitation affecting activities of daily living  
      *note must state this is met*
- [ ] **FALSE** — Active infection of the joint or of an adjacent surgical site  
      *note must state this is NOT met*
- [ ] **FALSE** — Body mass index of 45 or greater without documented weight management plan  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C044 — Attended polysomnography in a sleep laboratory (CPT 95810)

stratum `borderline` · gold **APPROVED**

> Patient: Evangelina Mbatha-Ross. MRN: 8895124. DOB: 03/18/1969. Referring clinician: L. Ferreiro, MD. Requesting CPT 95810, attended polysomnography in a sleep laboratory. Patient reports habitual snoring on most nights, two witnessed apnoeic episodes described by her husband in the past month, and daytime sleepiness with an Epworth Sleepiness Scale of 11, sufficient to constitute symptomatic sleep disordered breathing. Her medical history includes chronic obstructive pulmonary disease, GOLD stage 2, with an FEV1 of 63 percent predicted, on a long acting bronchodilator, and resting daytime oxygen saturation of 94 percent on room air. This chronic lung disease is present and, while moderate rather than severe, is sufficient to compromise the reliability of home sleep apnoea testing in her case, since overnight hypoventilation related desaturation cannot be distinguished from obstructive events on a limited channel ambulatory device. No home sleep study has been undertaken to date. Her presentation is one of sleep disordered breathing rather than primary insomnia; sleep onset latency is normal. Requesting review.

Confirm:

- [ ] **TRUE** — Documented symptoms of sleep disordered breathing such as habitual snoring, witnessed apnoea, or excessive daytime sleepiness  
      *note must state this is met*
- [ ] **TRUE** — Comorbid condition making home sleep apnoea testing unreliable, such as heart failure, chronic lung disease, or neuromuscular disease  
      *note must state this is met*
- [ ] **FALSE** — Prior home sleep apnoea test that was technically inadequate or negative despite persistent symptoms  
      *note must state this is NOT met*
- [ ] **FALSE** — Study requested solely for evaluation of insomnia without features of sleep disordered breathing  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C045 — Brain MRI with contrast (CPT 70553)

stratum `retrieval_distractor` · gold **APPROVED**

> Patient: Peregrine Nakashima. MRN: 3363780. DOB: 08/05/1993. Referring clinician: D. Iwuchukwu, MD. Requesting CPT 70553, MRI of the brain with and without contrast. Patient presented to the emergency department on 03 August 2026 with the abrupt onset of the worst headache of her life, accompanied by photophobia and vomiting. Neurological examination documents a new left sixth cranial nerve palsy with horizontal diplopia on left gaze and mild neck stiffness, constituting a focal neurological deficit accompanying a new onset headache. She has no prior headache history of any kind and has never taken preventive therapy for headache. Non-contrast CT head performed on presentation was reported as normal with no haemorrhage, no mass lesion, and no midline shift, and there are no imaging or examination findings suggesting an intracranial mass. She is acutely symptomatic and this is not a surveillance study. Separately, she is scheduled for elective coronary computed tomography angiography next month for atypical chest pain, unrelated to the present request. Requesting review.

Confirm:

- [ ] **TRUE** — Documented neurological sign or symptom prompting evaluation  
      *note must state this is met*
- [ ] **TRUE** — New onset headache accompanied by a focal neurological deficit  
      *note must state this is met*
- [ ] **FALSE** — Headache refractory to at least 3 months of standard preventive therapy  
      *note must state this is NOT met*
- [ ] **FALSE** — Clinical suspicion of intracranial mass with supporting examination findings  
      *note must state this is NOT met*
- [ ] **FALSE** — Study requested solely for routine surveillance in an asymptomatic patient  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

- [ ] mentions a second unrelated procedure (Coronary computed tomography angiography) that does not affect the criteria

---

## C046 — Roux-en-Y gastric bypass (CPT 43644)

stratum `retrieval_distractor` · gold **APPROVED**

> Patient: Anastasia Delacroix-Obiora. MRN: 7736925. DOB: 04/09/1987. Referring clinician: M. Hartnell, MD. Requesting CPT 43644, laparoscopic Roux-en-Y gastric bypass. Patient weighs 116 kg at a height of 1.71 m, giving a calculated body mass index of 39.7, which together with her documented obesity related comorbidity of type 2 diabetes exceeds the 35 threshold. Haemoglobin A1c is 8.6 percent on metformin and dulaglutide. She completed a medically supervised weight management programme from 11 September 2025 through 17 March 2026, six consecutive months, with monthly dietitian review, supervised exercise, and attendance recorded at 23 of 24 sessions. Preoperative psychological evaluation was completed 02 June 2026 by K. Aderinto, PsyD, documenting no untreated psychiatric illness, appropriate expectations, and formal clearance. She reports no alcohol use, no tobacco, and no recreational substance use, with a negative urine toxicology screen. She is not pregnant, has a copper intrauterine device in situ, and does not intend to conceive within the next two years. Separately, she is under orthopaedic follow up for a left shoulder impingement syndrome, unrelated to this request. Requesting review.

Confirm:

- [ ] **TRUE** — Body mass index of 40 or greater, or 35 or greater with an obesity related comorbidity  
      *note must state this is met*
- [ ] **TRUE** — Documented participation in a supervised weight management programme for at least 6 consecutive months  
      *note must state this is met*
- [ ] **TRUE** — Preoperative psychological evaluation completed and clearance documented  
      *note must state this is met*
- [ ] **FALSE** — Untreated substance use disorder  
      *note must state this is NOT met*
- [ ] **FALSE** — Pregnancy, current or planned within 12 months  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

- [ ] mentions a second unrelated procedure (Shoulder arthroscopy with rotator cuff repair) that does not affect the criteria

---

## C047 — Lumbar spine MRI without contrast (CPT 72148)

stratum `clear_approve` · gold **APPROVED**

> Patient: Bartholomeus Ndlovu. MRN: 4489163. DOB: 07/21/1961. Referring clinician: A. Rasmussen, MD. Requesting CPT 72148, MRI of the lumbar spine without contrast. Patient reports low back pain of 14 weeks duration, unremitting since onset and now waking him at night. He completed a nine week course of supervised physical therapy from 12 May 2026 to 14 July 2026, 18 sessions in total, including manual therapy, core stabilisation, and a graded home programme, without adequate relief. Review of systems documents an unintentional weight loss of 9 kg over three months and recurrent low grade fevers to 38.1 degrees, red flag features prompting concern. Examination shows full power throughout both lower limbs, symmetric and normal deep tendon reflexes, intact sensation in all dermatomes, and a negative straight leg raise bilaterally, with no focal neurological deficit identified. He has no bowel or bladder dysfunction and saddle sensation is preserved. No previous lumbar imaging of any modality has been performed. Requesting review.

Confirm:

- [ ] **TRUE** — Low back pain documented for at least 6 weeks  
      *note must state this is met*
- [ ] **TRUE** — Completed at least 4 weeks of supervised physical therapy without adequate relief  
      *note must state this is met*
- [ ] **FALSE** — Focal neurological deficit on examination  
      *note must state this is NOT met*
- [ ] **TRUE** — Red flag features present (unexplained weight loss, fever, history of malignancy, or bowel or bladder dysfunction)  
      *note must state this is met*
- [ ] **FALSE** — Lumbar MRI of the same region performed within the previous 6 months with no interval change in symptoms  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C048 — Hyperbaric oxygen therapy for diabetic foot ulcer (HCPCS G0277)

stratum `borderline` · gold **APPROVED**

> Patient: Clementine Achebe-Sorrell. MRN: 6617408. DOB: 09/12/1952. Referring clinician: J. Vanterpool, MD. Requesting HCPCS G0277, hyperbaric oxygen therapy for a chronic diabetic foot ulcer. Patient has type 2 diabetes of 17 years duration with established peripheral neuropathy. Ulcer over the plantar aspect of the left third metatarsal head, present since March 2026, measures 2.6 by 2.1 cm and probes through to tendon with visible deep tissue, documented as exactly Wagner grade 3. Standard wound care has been delivered for 31 days, from 08 July 2026 to 08 August 2026, including three sessions of sharp debridement, total contact casting for offloading, and dressing changes twice weekly, with wound area unchanged across the period. Vascular assessment on 05 August 2026 documents an ankle brachial index of 0.90 on the left, at the lower boundary of the normal range, with biphasic waveforms and periwound transcutaneous oximetry of 41 mmHg, sufficient to support healing. Chest radiograph on 05 August 2026 shows no pneumothorax. Requesting review.

Confirm:

- [ ] **TRUE** — Wagner grade 3 or higher diabetic foot ulcer documented  
      *note must state this is met*
- [ ] **TRUE** — Failed at least 30 days of standard wound care including debridement and offloading  
      *note must state this is met*
- [ ] **TRUE** — Adequate lower extremity perfusion confirmed by vascular assessment  
      *note must state this is met*
- [ ] **FALSE** — Untreated pneumothorax  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C049 — Hyperbaric oxygen therapy for diabetic foot ulcer (HCPCS G0277)

stratum `clear_deny` · gold **DENIED**

> Patient: Aurelius Kwarteng. MRN: 3341276. DOB: 01/06/1959. Referring clinician: P. Osunde, MD. Requesting HCPCS G0277, hyperbaric oxygen therapy for a diabetic foot ulcer. Patient has type 2 diabetes of 24 years duration. Ulcer over the right hallux, present since April 2026, measures 3.3 by 2.7 cm with probing to bone and radiographic changes consistent with underlying osteomyelitis, documented as Wagner grade 3. Regarding prior treatment, the wound was first assessed at this clinic 11 days ago on 29 July 2026. Since then he has undergone a single sharp debridement and has been issued a removable cast walker; the total duration of standard wound care to date is therefore 11 days, well short of a 30 day trial, and the offloading and dressing regimen has only just been established. Vascular assessment on 31 July 2026 documents an ankle brachial index of 0.94 with triphasic waveforms and periwound transcutaneous oximetry of 46 mmHg, indicating adequate perfusion. Chest radiograph clear with no pneumothorax. Requesting review.

Confirm:

- [ ] **TRUE** — Wagner grade 3 or higher diabetic foot ulcer documented  
      *note must state this is met*
- [ ] **FALSE** — Failed at least 30 days of standard wound care including debridement and offloading  
      *note must state this is NOT met*
- [ ] **TRUE** — Adequate lower extremity perfusion confirmed by vascular assessment  
      *note must state this is met*
- [ ] **FALSE** — Untreated pneumothorax  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C050 — Shoulder arthroscopy with rotator cuff repair (CPT 29827)

stratum `clear_approve` · gold **APPROVED**

> Patient: Melisande Oyewole-Grant. MRN: 8862017. DOB: 06/28/1978. Referring clinician: R. Beaumont, MD. Requesting CPT 29827, arthroscopic rotator cuff repair, right shoulder. MRI dated 21 May 2026 demonstrates a full thickness tear of the supraspinatus tendon measuring 2.1 cm in anteroposterior dimension with 11 mm of retraction, fluid tracking into the subacromial subdeltoid bursa, and an intact infraspinatus and subscapularis. Conservative management has run 17 weeks and included 22 supervised physical therapy sessions across two courses, two subacromial corticosteroid injections, NSAIDs, and activity modification, without functional recovery. On examination there is 3 out of 5 strength on empty can testing with a positive external rotation lag sign and demonstrable weakness of the affected shoulder compared with the contralateral side. Onset was insidious over eight months without an identified traumatic event, and she is 48 years of age. Glenohumeral joint spaces are preserved with a normal acromiohumeral interval of 9 mm and no arthritic change or cuff arthropathy. Requesting review.

Confirm:

- [ ] **TRUE** — Imaging confirmation of a full thickness rotator cuff tear  
      *note must state this is met*
- [ ] **TRUE** — Failed conservative management for at least 6 weeks including physical therapy  
      *note must state this is met*
- [ ] **TRUE** — Persistent weakness on examination of the affected shoulder  
      *note must state this is met*
- [ ] **FALSE** — Acute traumatic tear in a patient under 60 years of age  
      *note must state this is NOT met*
- [ ] **FALSE** — Advanced glenohumeral arthritis or established rotator cuff arthropathy  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C051 — Roux-en-Y gastric bypass (CPT 43644)

stratum `clear_approve` · gold **APPROVED**

> Patient: Ignacio Balogun-Fairweather. MRN: 5594830. DOB: 10/15/1990. Referring clinician: T. Nkosi, MD. Requesting CPT 43644, laparoscopic Roux-en-Y gastric bypass. Patient weighs 149 kg at a height of 1.82 m, giving a calculated body mass index of 45.0, exceeding the 40 threshold on its own. Comorbidities include obstructive sleep apnoea on CPAP, non-alcoholic fatty liver disease on ultrasound, and hypertension on two agents. He completed a medically supervised weight management programme at this centre from 21 August 2025 through 26 February 2026, six consecutive months, attending 24 of 26 scheduled dietitian, exercise physiology, and behavioural sessions. Preoperative psychological evaluation was performed 09 June 2026 by M. Castellanos, PsyD, who documented realistic expectations, understanding of the postoperative dietary and supplementation requirements, no active eating disorder, and clearance to proceed without qualification. He reports no alcohol intake, has never smoked, and denies recreational substance use, confirmed on a negative screen dated 09 June 2026. He is male and pregnancy is not applicable. Requesting review.

Confirm:

- [ ] **TRUE** — Body mass index of 40 or greater, or 35 or greater with an obesity related comorbidity  
      *note must state this is met*
- [ ] **TRUE** — Documented participation in a supervised weight management programme for at least 6 consecutive months  
      *note must state this is met*
- [ ] **TRUE** — Preoperative psychological evaluation completed and clearance documented  
      *note must state this is met*
- [ ] **FALSE** — Untreated substance use disorder  
      *note must state this is NOT met*
- [ ] **FALSE** — Pregnancy, current or planned within 12 months  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C052 — Coronary computed tomography angiography (CPT 75574)  **FLAGGED**

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Rosamund Ekechukwu. MRN: 2273594. DOB: 02/03/1971. Referring clinician: D. Marchetti, MD. Requesting CPT 75574, coronary computed tomography angiography. Patient is referred following an abnormal calcium score of 84 obtained during a screening study arranged privately. Regarding symptoms, the referral letter does not describe chest pain, dyspnoea, or any anginal equivalent, and at today's telephone consultation the patient could not be reached to characterise her presentation; no symptom history is recorded in the chart. Her documented pretest probability of obstructive coronary artery disease, calculated from age, sex, and risk factors comprising treated hypertension and an LDL of 141 mg/dL, is 12 percent, within the low to intermediate range. She has never undergone invasive coronary angiography and carries no diagnosis of established obstructive coronary disease. Serum creatinine 0.7 mg/dL with an estimated glomerular filtration rate of 94 mL/min/1.73m2, and no contrast allergy is recorded. Requesting review.

Confirm:

- [ ] **ABSENT** — Symptoms suggestive of coronary artery disease such as chest pain or anginal equivalent  
      *note must NOT establish this either way*
- [ ] **TRUE** — Low to intermediate pretest probability of obstructive coronary disease documented  
      *note must state this is met*
- [ ] **FALSE** — Known obstructive coronary artery disease already confirmed on invasive angiography  
      *note must state this is NOT met*
- [ ] **FALSE** — Estimated glomerular filtration rate below 30 without nephrology clearance  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C053 — Lumbar spine MRI without contrast (CPT 72148)

stratum `retrieval_distractor` · gold **APPROVED**

> Patient: Cassius Whitmore-Adeyemi. MRN: 9945602. DOB: 11/26/1964. Referring clinician: L. Fontaine, MD. Requesting CPT 72148, MRI of the lumbar spine without contrast. Patient reports low back pain of 16 weeks duration, constant since onset with no symptom free interval. He completed a supervised physical therapy course of 11 weeks duration from 28 April 2026 to 16 July 2026, 21 sessions comprising manual therapy, McKenzie extension protocol, and progressive core stabilisation, without adequate relief. Review of systems documents an unintentional weight loss of 8 kg over four months together with drenching night sweats, red flag features in this context. Examination demonstrates 5 out of 5 power throughout both lower limbs, symmetric patellar and Achilles reflexes, normal sensation in all lumbar and sacral dermatomes, and a negative straight leg raise bilaterally; no focal neurological deficit is present. He has had no prior lumbar spine imaging. Separately, he is awaiting an outpatient coronary computed tomography angiography arranged by cardiology for atypical chest discomfort, unrelated to this request. Requesting review.

Confirm:

- [ ] **TRUE** — Low back pain documented for at least 6 weeks  
      *note must state this is met*
- [ ] **TRUE** — Completed at least 4 weeks of supervised physical therapy without adequate relief  
      *note must state this is met*
- [ ] **FALSE** — Focal neurological deficit on examination  
      *note must state this is NOT met*
- [ ] **TRUE** — Red flag features present (unexplained weight loss, fever, history of malignancy, or bowel or bladder dysfunction)  
      *note must state this is met*
- [ ] **FALSE** — Lumbar MRI of the same region performed within the previous 6 months with no interval change in symptoms  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

- [ ] mentions a second unrelated procedure (Coronary computed tomography angiography) that does not affect the criteria

---

## C054 — Total hip arthroplasty (CPT 27130)

stratum `borderline` · gold **APPROVED**

> Patient: Philippa Osei-Trethewey. MRN: 4427185. DOB: 05/02/1949. Referring clinician: A. Kirchner, MD. Requesting CPT 27130, total hip arthroplasty, right hip. Radiographs dated 14 July 2026 demonstrate advanced right hip osteoarthritis with superolateral joint space narrowing to less than 1 mm, subchondral sclerosis, and acetabular osteophyte formation. Conservative management commenced 08 April 2026 and has now run exactly three months and one week, comprising paracetamol and topical NSAIDs, 14 supervised physical therapy sessions, and a fluoroscopically guided intra-articular corticosteroid injection on 20 May 2026 which gave four weeks of partial relief before symptoms returned to baseline. She reports pain waking her from sleep on five or six nights each week, requiring repositioning and frequently a night time analgesic dose before she can settle again. She continues to manage a 500 metre walk to her local shop with two rest stops, and pain is not the factor that halts her. No fever, no erythema, no wound, no evidence of local or systemic infection. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic evidence of advanced hip osteoarthritis, avascular necrosis, or displaced femoral neck fracture  
      *note must state this is met*
- [ ] **TRUE** — Failed conservative management for at least 3 months, or an acute fracture indication making conservative management inappropriate  
      *note must state this is met*
- [ ] **FALSE** — Pain limiting ambulation to less than one block  
      *note must state this is NOT met*
- [ ] **TRUE** — Night pain disturbing sleep on most nights  
      *note must state this is met*
- [ ] **FALSE** — Active local or systemic infection  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C055 — Lumbar spinal fusion, single level (CPT 22612)  **FLAGGED**

stratum `documentation_gap` · gold **MORE_INFO**

> Patient: Leopold Nwachukwu-Vance. MRN: 6688431. DOB: 08/19/1967. Referring clinician: S. Brandtner, MD. Requesting CPT 22612, single level lumbar fusion at L4-L5. Flexion-extension radiographs dated 12 July 2026 demonstrate grade 1 degenerative spondylolisthesis at L4-L5 with 7 mm of anterolisthesis increasing to 10 mm on flexion, confirming segmental instability at the operative level. His symptoms comprise neurogenic claudication with bilateral L5 radicular pain, reproduced on provocative testing and confirmed concordant on selective L5 nerve root block, correlating with the level demonstrated on imaging. Regarding non-operative treatment, he states he has had injections and physiotherapy over the years at various clinics, but the number of sessions, the dates, and the total duration could not be established at today's consultation, and no external records have been received despite requests to two named providers. He has never smoked. DEXA dated 27 January 2026 records a lowest T-score of negative 1.9. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic confirmation of spondylolisthesis or segmental instability at the operative level  
      *note must state this is met*
- [ ] **TRUE** — Failed at least 6 months of non-operative management including physical therapy  
      *note must state this is met*
- [ ] **ABSENT** — Concordant symptoms correlating with the imaged level  
      *note must NOT establish this either way*
- [ ] **FALSE** — Active nicotine use without documented cessation counselling  
      *note must state this is NOT met*
- [ ] **FALSE** — Untreated osteoporosis with T-score below negative 2.5  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C056 — Brain MRI with contrast (CPT 70553)

stratum `clear_approve` · gold **APPROVED**

> Patient: Persephone Adeoye-Lindgren. MRN: 3358029. DOB: 12/11/1983. Referring clinician: H. Petrossian, MD. Requesting CPT 70553, MRI of the brain with and without contrast. Patient presents with a five week history of progressive morning headache with associated vomiting, together with new onset clumsiness of the left hand. Neurological examination documents left sided dysmetria on finger to nose testing, an intention tremor, and a wide based ataxic gait, constituting definite neurological signs prompting evaluation. Fundoscopy shows bilateral papilloedema. Non-contrast CT head performed 06 August 2026 demonstrates a 2.2 cm hyperdense right cerebellar lesion with surrounding oedema and early fourth ventricular effacement, findings that raise clinical suspicion of an intracranial mass and are supported by the corresponding cerebellar signs on examination. She has no history of migraine and has never been prescribed preventive headache therapy. Her headache is new in onset and is not accompanied by a focal deficit of the type seen in migraine with aura. She is symptomatic and this is not routine surveillance. Requesting review.

Confirm:

- [ ] **TRUE** — Documented neurological sign or symptom prompting evaluation  
      *note must state this is met*
- [ ] **FALSE** — New onset headache accompanied by a focal neurological deficit  
      *note must state this is NOT met*
- [ ] **FALSE** — Headache refractory to at least 3 months of standard preventive therapy  
      *note must state this is NOT met*
- [ ] **TRUE** — Clinical suspicion of intracranial mass with supporting examination findings  
      *note must state this is met*
- [ ] **FALSE** — Study requested solely for routine surveillance in an asymptomatic patient  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C057 — Group 2 power wheelchair (HCPCS K0823)

stratum `clear_approve` · gold **APPROVED**

> Patient: Augustine Karlsson-Mbeki. MRN: 8871945. DOB: 03/07/1943. Referring clinician: R. Solheim, MD. Requesting HCPCS K0823, Group 2 power wheelchair. Patient has severe chronic obstructive pulmonary disease with an FEV1 of 28 percent predicted and marked exertional desaturation, together with deconditioning following two hospital admissions this year. He desaturates to 84 percent walking six metres and cannot reach his kitchen or bathroom from his chair without stopping and recovering; he is unable to complete meal preparation, toileting, or bathing within the home as a direct result. Occupational therapy specialty mobility evaluation was completed 16 June 2026 by P. Danquah, OTR/L, within the past six months. A manual wheelchair was trialled over seven weeks; self-propulsion provoked immediate dyspnoea and desaturation to 86 percent within 20 seconds, and it does not meet his needs. He operated a demonstration power chair with correct control, safe stopping, and appropriate obstacle negotiation, and his daughter, who lives with him, is available as a secondary operator. Home assessment documents a single level dwelling with level threshold access and 36 inch internal doorways requiring no modification. Requesting review.

Confirm:

- [ ] **TRUE** — Mobility limitation preventing completion of activities of daily living within the home  
      *note must state this is met*
- [ ] **TRUE** — Specialty evaluation by a licensed therapist completed within the previous 6 months  
      *note must state this is met*
- [ ] **TRUE** — Patient demonstrates capacity to operate the device safely, or a caregiver is available to operate it  
      *note must state this is met*
- [ ] **FALSE** — A manual wheelchair or lesser mobility device adequately meets the patient's needs  
      *note must state this is NOT met*
- [ ] **FALSE** — Home environment cannot accommodate the device and no modification is planned  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C058 — Continuous positive airway pressure device (HCPCS E0601)

stratum `clear_deny` · gold **DENIED**

> Patient: Wilhelmina Fitzgerald-Osei. MRN: 5536718. DOB: 09/23/1976. Referring clinician: T. Ravensworth, MD. Requesting HCPCS E0601, continuous positive airway pressure device. Patient has been referred with a clinical suspicion of obstructive sleep apnoea. Regarding diagnostic testing, no sleep study has been performed. A home sleep apnoea test was ordered on 19 June 2026 but has not yet been undertaken, and no attended polysomnography has been carried out at this or any other institution at any point; there is therefore no diagnostic study within the preceding twelve months or at all. Face to face clinical evaluation was completed by the undersigned on 06 August 2026 in advance of this order, documenting habitual snoring, witnessed apnoeas reported by her partner, an Epworth Sleepiness Scale of 15, morning headaches, a body mass index of 38.4, and a neck circumference of 41 cm. She has not previously trialled positive airway pressure and no interface intolerance is recorded. Requesting review.

Confirm:

- [ ] **FALSE** — Diagnostic sleep study completed within the previous 12 months  
      *note must state this is NOT met*
- [ ] **ABSENT** — Apnoea hypopnoea index of 15 or greater, or 5 or greater with documented symptoms or cardiovascular comorbidity  
      *note must NOT establish this either way*
- [ ] **TRUE** — Face to face clinical evaluation by the treating clinician documented prior to the order  
      *note must state this is met*
- [ ] **FALSE** — Documented inability to tolerate positive airway pressure with no alternative interface trialled  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---

## C059 — Attended polysomnography in a sleep laboratory (CPT 95810)

stratum `retrieval_distractor` · gold **APPROVED**

> Patient: Ezekiel Vandermolen. MRN: 2219683. DOB: 04/30/1965. Referring clinician: K. Achterberg, MD. Requesting CPT 95810, attended polysomnography in a sleep laboratory. Patient reports habitual snoring every night, multiple witnessed apnoeic pauses described by his wife, and marked excessive daytime sleepiness with an Epworth Sleepiness Scale of 16, including falling asleep at his desk on several occasions. A home sleep apnoea test was performed 14 March 2026 and was technically adequate with 6 hours 30 minutes of valid recording; it returned an apnoea hypopnoea index of 3.4, a negative result, yet his symptoms have persisted unchanged and have worsened since. Body mass index 37.2, Mallampati class IV, neck circumference 45 cm. He has no heart failure, no chronic lung disease, and no neuromuscular disorder. His presentation is one of sleep disordered breathing rather than insomnia; sleep onset latency is under ten minutes. Separately, he is scheduled for lumbar spine MRI next week for chronic low back pain, unrelated to the present request. Requesting review.

Confirm:

- [ ] **TRUE** — Documented symptoms of sleep disordered breathing such as habitual snoring, witnessed apnoea, or excessive daytime sleepiness  
      *note must state this is met*
- [ ] **FALSE** — Comorbid condition making home sleep apnoea testing unreliable, such as heart failure, chronic lung disease, or neuromuscular disease  
      *note must state this is NOT met*
- [ ] **TRUE** — Prior home sleep apnoea test that was technically inadequate or negative despite persistent symptoms  
      *note must state this is met*
- [ ] **FALSE** — Study requested solely for evaluation of insomnia without features of sleep disordered breathing  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

- [ ] mentions a second unrelated procedure (Lumbar spine MRI without contrast) that does not affect the criteria

---

## C060 — Total knee arthroplasty (CPT 27447)

stratum `clear_approve` · gold **APPROVED**

> Patient: Theodora Chukwuemeka-Vale. MRN: 6642398. DOB: 07/16/1955. Referring clinician: D. Amankwah, MD. Requesting CPT 27447, total knee arthroplasty, left knee. Standing radiographs dated 24 June 2026 demonstrate complete medial compartment joint space obliteration with bone on bone apposition, large marginal osteophytes, extensive subchondral sclerosis and cyst formation, and 12 degrees of varus deformity, reported as Kellgren-Lawrence grade 4. Conservative management has extended over 16 months and comprised naproxen and topical NSAIDs, three courses of supervised physical therapy totalling 34 sessions, two intra-articular corticosteroid injections, an unloader brace, and a walking stick, with steady deterioration throughout. She is unable to walk to her garden gate, has given up her weekly swimming, cannot manage stairs without both a handrail and assistance, and now requires help with washing her feet and putting on socks. Body mass index 34.1 and stable over 12 months. No fever, no effusion, no warmth or erythema, no skin breakdown, and no recent dental, urinary, or skin infection; CRP 3 mg/L and white cell count normal. Requesting review.

Confirm:

- [ ] **TRUE** — Radiographic evidence of advanced osteoarthritis (Kellgren-Lawrence grade 3 or 4)  
      *note must state this is met*
- [ ] **TRUE** — Failed conservative management for at least 3 months including NSAIDs and physical therapy  
      *note must state this is met*
- [ ] **TRUE** — Documented functional limitation affecting activities of daily living  
      *note must state this is met*
- [ ] **FALSE** — Active infection of the joint or of an adjacent surgical site  
      *note must state this is NOT met*
- [ ] **FALSE** — Body mass index of 45 or greater without documented weight management plan  
      *note must state this is NOT met*
- [ ] note states no decision and no recommendation
- [ ] note contains a fictional name, MRN and DOB

---
