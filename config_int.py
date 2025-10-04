import os

VERSION_NAME = "DDIG_v1.0.0"

PATH_ROOT_I = r"C:\Users\MINOLI\Projects\DDIG-2022-08-23\DDIG"

INTERNAL_VALIDATION = True

PATH_INPUT_CLAIMS = os.path.join(PATH_ROOT_I, r"ddi_input\ClaimsToGroup.csv")
PATH_INPUT_ENROLMENT = os.path.join(PATH_ROOT_I, r"ddi_input\EnrollmentToGroup.csv")
PATH_INPUT_MEMBERS = os.path.join(PATH_ROOT_I, r"ddi_input\MembersToGroup.csv")

PATH_OUTPUT_DDI_G_CLAIM = os.path.join(PATH_ROOT_I, r"ddi_output\DDIGClaimOutput.csv")
PATH_OUTPUT_DDI_G_CONFINEMENT = os.path.join(PATH_ROOT_I, r"ddi_output\DDIGConfinementOutput.csv")
PATH_OUTPUT_DDI_G_SUMMARY = os.path.join(PATH_ROOT_I, r"ddi_output\DDIGSummaryOutput.csv")
PATH_OUTPUT_DDI_G_CONTROL_REPORT = os.path.join(PATH_ROOT_I, r"ddi_output\ControlReport.txt")

PATH_MAIN_REF_GROUPER = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\ddig_icd_codes_ref\ddig_icd_10_codes_ref.csv")

PATH_REF_SEVERITY_DDIG = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\ddig_icd_codes_ref\ddig_base_severity_ref.csv")

PATH_MAIN_REF_ICD_9_10 = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\ddig_icd_codes_ref\icd_9_10_ref.csv")

PATH_MAIN_REF_NDC = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\ndc_ref\all_ndc_drug_rxnorm_ddig_ref.csv")

PATH_MAIN_REF_ALL_NDC = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\ndc_ref\all_ndc_drug_dic.json")

PATH_REF_DRUG_OFV = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\ndc_ref\drug_ofv_ref.csv")

PATH_REF_DRUG_CLS = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\ndc_ref\drug_cls_ref.csv")

PATH_REF_DRUG_TYPE = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\ndc_ref\drug_type_ref.csv")

PATH_MAIN_REF_PROCEDURE_CODES = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\procedure_revenue_codes_ref\proc_codes_dic.json")

PATH_MAIN_REF_ALL_REVENUE_CODES = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\procedure_revenue_codes_ref\all_revenu_codes_dic.json")

PATH_MAIN_REF_REVENUE_CODE_RECORD_TYPE = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\procedure_revenue_codes_ref\revenu_code_record_type_dic.json")

PATH_MAIN_REF_CPT_RECORD_TYPE = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\procedure_revenue_codes_ref\cpt_record_type_dic.json")

PATH_MAIN_REF_M_CODE_RECORD_TYPE = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\procedure_revenue_codes_ref\m_code_record_type_dic.json")

PATH_MAIN_REF_Z_RECORD_TYPE = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\procedure_revenue_codes_ref\z_record_type_dic.json")

PATH_REF_CPT_CATEGORY_I_RT = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\procedure_revenue_codes_ref\cpt_I_record_type_dic.json")

PATH_REF_CPT_I_CONTRAST = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\procedure_revenue_codes_ref\cpt_70010_79999_w_contrast_dic.json")

PATH_REF_PROC_OFV = os.path.join(
    PATH_ROOT_I,
    r"reference_tables\procedure_revenue_codes_ref\proc_ofv_ref.csv")

PATH_ROOT_II = r"C:\Users\MINOLI\Projects\DDIG-2022-08-23\ETG"

PATH_ETG_CLAIMS_TEXT = os.path.join(PATH_ROOT_II, r"output\ETGClaimsOutput.txt")
PATH_ETG_CLAIMS_CSV = os.path.join(PATH_ROOT_II, r"output\ETGClaimsOutput.csv")
PATH_ETG_CONF_TEXT = os.path.join(PATH_ROOT_II, r"output\ETGConfinement.txt")
PATH_ETG_CONF_CSV = os.path.join(PATH_ROOT_II, r"output\ETGConfinement.csv")
PATH_ETG_MEM_TEXT = os.path.join(PATH_ROOT_II, r"output\EtgSummary.txt")
PATH_ETG_MEM_CSV = os.path.join(PATH_ROOT_II, r"output\EtgSummary.csv")

PATH_ETG_NUM_REF_CSV = os.path.join(PATH_ROOT_I, r"reference_tables\etg_ref\etg_des.csv")
PATH_ETG_CP_REF_CSV = os.path.join(PATH_ROOT_I, r"reference_tables\etg_ref\etg_base_cp.csv")

PATH_VALIDATION_FOLDER = os.path.join(PATH_ROOT_I, r"ddi_output\validation")
PATH_INTERNAL_VALIDATION_REPORT = os.path.join(PATH_ROOT_I, r"ddi_output\validation\InternalValidationReport.txt")
PATH_MERGED_CLAIMS = os.path.join(PATH_ROOT_I, r"ddi_output\validation\MergedClaimOutput.csv")
PATH_DDI_CLM_TEST = os.path.join(PATH_ROOT_I, r"ddi_output\validation\TestClaimResults.csv")
PATH_EPI_CONF_TEST = os.path.join(PATH_ROOT_I, r"ddi_output\validation\TestEpisodeConfinementResults.csv")
PATH_CONF_TEST = os.path.join(PATH_ROOT_I, r"ddi_output\validation\TestConfinementResults.csv")
PATH_SMY_TEST = os.path.join(PATH_ROOT_I, r"ddi_output\validation\TestSummaryResults.csv")




