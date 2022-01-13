import os

import pdfkit
 # from src.configs.constants import INDEX_PATH
def make_index_page():
    html_template =f"""<!DOCTYPE html>
                         <html>
                         <head>
                         <meta name="pdfkit-page-size" content="Legal" />
                         <meta name="pdfkit-orientation" content="Landscape" />
                         <meta charset="utf-8" />
                         </head>
                         <body>
                         <table width="100%" border="1" style="border-collapse: collapse;" cellspacing="4px" cellpadding="4px">
                         <tr>
                         <td>SC India Agenda</td>
                         <td></td>
                         <td></td>
                         <td></td>
                         <td></td>
                         <td></td>
                         <td>meeting_date </td>
                         </tr>
                         <tr>
                         <td>Potential Exits</td>
                         <td></td>
                         <td>Team</td>
                         <td></td>
                         <td></td>
                         <td></td>
                         <td></td>
                         </tr>
                         <tr>
                         <td>Public Market Report</td>
                         <td></td>
                         <td>Team</td>
                         <td></td>
                         <td></td>
                         <td></td>
                         <td></td>
                         </tr>
                         <tr>
                         <td style="background-color: #c8c8c8;width: 15%;">Investment Discussion</td>
                         <td style="background-color: #c8c8c8;width: 18%;">Company<br />
                             Including Ticker for Listed Co</td>
                         <td style="background-color: #c8c8c8;">Team</td>
                         <td style="background-color: #c8c8c8;">Description</td>
                         <td style="background-color: #c8c8c8; text-align: center;width: 5%;">Existing</td>
                         <td style="background-color: #c8c8c8;text-align: center;width: 8%;">Discussion</td>
                         <td style="background-color: #c8c8c8;text-align: center;width: 8%;">UID</td>
                         </tr>
                         <tr>
         company_data
                             <tr>
                             <td colspan="2" style="background-color: #c8c8c8;">Common Items</td>
                             <td></td>
                             <td></td>
                             <td></td>
                             <td></td>
                             <td></td>
                             </tr>
                             <tr>
                             <td>Deal Closings</td>
                             <td></td>
                             <td>Harshal</td>
                             <td></td>
                             <td></td>
                             <td></td>
                             <td></td>
                             </tr>
                             </table>
                         </body>
                             </html>
     """
    pdfkit.from_string(html_template, '/home/pc/code/index.pdf')


print(os.getcwd())
make_index_page()