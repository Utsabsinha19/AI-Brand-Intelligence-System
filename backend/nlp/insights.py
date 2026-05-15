def generate_insight(negative_percent, complaint_percent):

    if negative_percent > 50:

        return (
            "Consumers are expressing strong dissatisfaction "
            "towards the brand. Immediate action is recommended."
        )

    elif complaint_percent > 40:

        return (
            "Customer complaints are rising rapidly. "
            "Support and logistics should be reviewed."
        )

    else:

        return (
            "Overall consumer sentiment appears stable "
            "with manageable complaint levels."
        )