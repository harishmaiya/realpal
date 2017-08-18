AGENT_USER = 0
CLIENT_USER = 1
PURCHASE_STEP_CHOICES = (
        ('DAP', 'Decide and Prepare'),
        ('EAO', 'Evaluate and Offer'),
        ('HOB', 'Home owner benefits'),
    )

STATUS_CHOICES = (
        ('SI', 'Single'),
        ('MNK', 'Married with No Kids'),
        ('MNSK', 'Married with No School Kids'),
        ('MSK', 'Married with School Kids'),
        ('INV', 'Investor')
    )

HOUSE_TYPE_CHOICES = (
        ('SF', 'Single Family'),
        ('TH', 'Townhome'),
        ('CN', 'Condominium'),
        ('NC', 'New Construction'),
        ('OT', 'Other Options'),
        ('FX', 'Flexible')
    )

HOUSE_AGE_CHOICES = (
        ('NC', 'New Construction'),
        ('15', 'One to Fifteen'),
        ('30', 'Fifteen to thirty'),
        ('OLD', 'Over thirty')
    )

HOUSE_CONDITION_CHOICES = (
        ('UP', 'Updated'),
        ('SL', 'Slightly dated'),
        ('FU', 'Fixer Upper')
    )

NEIGHBORHOOD_TYPE = (
        ('HD', 'High Density'),
        ('MD', 'Medium Density'),
        ('LD', 'Low Density'),
        ('AW', 'Anywhere')
    )

HOW_SOON_CHOICES = (
        ('3', '0-3 Months'),
        ('6', '3-6 Months'),
        ('12', '6-12 Months'),
        ('12+', '12+ Months'),
        ('SK', 'Skip')
    )

LANGUAGE_CHOICES = (
        ('EN', 'English'),
        ('ESP', 'Spanish'),
        ('CA', 'Mandarin/Cantonese'),
        ('HI', 'Hindi'),
        ('OT', 'Other'),
    )

CREDIT_SCORE_CHOICES = (
        ('780+', '780+'),
        ('740-779', '740-779'),
        ('700-739', '700-739'),
        ('650-699', '650-699'),
        ('600-649', '600-649'),
        ('<599', '<599')
    )
