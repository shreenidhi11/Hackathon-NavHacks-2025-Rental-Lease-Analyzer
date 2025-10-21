from pydantic import BaseModel, Field

class Lease(BaseModel):
    '''
    Data Model for Lease
    '''

    # --- Money related questions ---
    security_deposit: str = Field(description="Total amount of the security deposit (e.g., '$2000').")
    deposit_conditions: str = Field(
        description="Summary of conditions for losing the deposit (e.g., 'Damage beyond normal wear, unpaid rent, cleaning fees').")
    non_refundable_fees: str = Field(
        description="List any non-refundable fees (e.g., 'Move-in fee: $500, Pet fee: $250').")
    late_fee_policy: str = Field(
        description="The policy for late rent (e.g., '$50 fee if paid after the 5th of the month').")

    # --- Moving Out related questions ---
    termination_notice: str = Field(
        description="The required notice period before the lease ends (e.g., '60 days written notice').")
    early_termination_penalty: str = Field(
        description="The penalty for breaking the lease early (e.g., 'Must pay 2 months' rent').")
    auto_renewal_clause: str = Field(
        description="Does the lease auto-renew? (e.g., 'Yes, renews month-to-month' or 'Yes, renews for 1 year').")

    # --- Living there related questions ---
    pet_policy: str = Field(
        description="Summary of pet rules (e.g., 'Allowed, $50/month pet rent, 40lb weight limit').")
    guest_policy: str = Field(
        description="Summary of guest rules (e.g., 'Guests allowed for up to 14 consecutive days').")
    subletting_policy: str = Field(
        description="Is subletting allowed? (e.g., 'Not allowed without written landlord consent').")
    maintenance_and_repairs: str = Field(
        description="Who is responsible for repairs (e.g., 'Tenant responsible for minor repairs, landlord for major systems').")
    utilities_included: str = Field(
        description="List all utilities paid by the landlord (e.g., 'Water and trash. Tenant pays gas and electric.').")