
import uuid

# Department mapping
DEPARTMENT_MAPPING = {
    "Technical": "Engineering",
    "Billing": "Finance",
    "Account": "Account Support",
    "Other": "General Support"
}


def route_ticket(category: str, priority: str):
    # Assign department using category
    department = DEPARTMENT_MAPPING.get(
        category, "General Support"
    )

    # Escalate high-priority tickets
    escalation_required = priority == "High"

    # Generate unique ticket ID
    ticket_id = "TKT-" + uuid.uuid4().hex[:8].upper()

    return ticket_id, department, escalation_required
