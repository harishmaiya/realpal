AGENT_USER = 0
CLIENT_USER = 1

USER_TYPE_CHOICES = (
        (AGENT_USER, 'Agent'),
        (CLIENT_USER, 'Client')
    )

PS_DAP = 0
PS_EAO = 1
PS_HOB = 2

PURCHASE_STEP_CHOICES = (
        (PS_DAP, 'Decide and Prepare'),
        (PS_EAO, 'Evaluate and Offer'),
        (PS_HOB, 'Home owner benefits'),
    )

SC_SI = 0
SC_MNK = 1
SC_MNSK = 2
SC_MSK = 3
SC_INV = 4

STATUS_CHOICES = (
        (SC_SI, 'Single'),
        (SC_MNK, 'Married with No Kids'),
        (SC_MNSK, 'Married with No School Kids'),
        (SC_MSK, 'Married with School Kids'),
        (SC_INV, 'Investor')
    )

HT_SF = 0
HT_TH = 1
HT_CN = 2
HT_NC = 3
HT_OT = 4
HT_FX = 5

HOUSE_TYPE_CHOICES = (
        (HT_SF, 'Single Family'),
        (HT_TH, 'Townhome'),
        (HT_CN, 'Condominium'),
        (HT_NC, 'New Construction'),
        (HT_OT, 'Other Options'),
        (HT_FX, 'Flexible')
    )

HA_NC = 0
HA_15 = 1
HA_30 = 2
HA_OLD = 3

HOUSE_AGE_CHOICES = (
        (HA_NC, 'New Construction'),
        (HA_15, 'One to Fifteen'),
        (HA_30, 'Fifteen to thirty'),
        (HA_OLD, 'Over thirty')
    )

HC_UP = 0
HC_SL = 1
HC_FU = 2

HOUSE_CONDITION_CHOICES = (
        (HC_UP, 'Updated'),
        (HC_SL, 'Slightly dated'),
        (HC_FU, 'Fixer Upper')
    )

NT_HD = 0
NT_MD = 1
NT_LD = 2
NT_AW = 3

NEIGHBORHOOD_TYPE = (
        (NT_HD, 'High Density'),
        (NT_MD, 'Medium Density'),
        (NT_LD, 'Low Density'),
        (NT_AW, 'Anywhere')
    )

HS_3 = 0
HS_6 = 1
HS_12 = 2
HS_12P = 3
HS_SK = 4

HOW_SOON_CHOICES = (
        (HS_3, '0-3 Months'),
        (HS_6, '3-6 Months'),
        (HS_12, '6-12 Months'),
        (HS_12P, '12+ Months'),
        (HS_SK, 'Skip')
    )

LC_EN = 0
LC_ESP = 1
LC_CA = 2
LC_HI = 3
LC_OT = 4


LANGUAGE_CHOICES = (
        (LC_EN, 'English'),
        (LC_ESP, 'Spanish'),
        (LC_CA, 'Mandarin/Cantonese'),
        (LC_HI, 'Hindi'),
        (LC_OT, 'Other'),
    )

CS_780P = 0
CS_740P = 1
CS_700P = 2
CS_650P = 3
CS_600P = 4
CS_599P = 5


CREDIT_SCORE_CHOICES = (
        (CS_780P, '780+'),
        (CS_740P, '740-779'),
        (CS_700P, '700-739'),
        (CS_650P, '650-699'),
        (CS_600P, '600-649'),
        (CS_599P, '<599')
    )
