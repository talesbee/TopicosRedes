# Mostrar os projeots no servidor

import gns3fy

from tabulate import tabulate
servidor = gns3fy.Gns3Connector("http://localhost:3080")

print(
        tabulate(
            servidor.projects_summary(is_print=False),
            headers=["Project Name", "Project ID", "Total Nodes", "Total Links", "Status"],
        )
    )


