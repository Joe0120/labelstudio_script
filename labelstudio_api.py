import requests, json

headers = {
  'Accept': '*/*',
  'Cookie': '_ga=GA1.1.659053664.1688443671; csrftoken=V0a77A0tlhA09Co0pPPONGJOrFvTvSaJwpSnsHg1nPTmEu9b7LyWOV2et6sZdrYt; _ga_Z4KXEBY4VP=GS1.1.1688443671.1.0.1688443679.52.0.0; sessionid=.eJxVj81uxCAMhN-F8yYCYv5y7L3PEJlgEroRrEIi9Ud995JqL3vwwTOfZ-QfdqbARqYNASgVuzlG04GVqrPSmM4rFFGRDkCO3VjZF8zpG49U8vS4s1Hc2Ib1mLaypNxWbS3AoI3rtXZykM2f8DzW6ay0T_9Vgr1oHuc75csIH5iX0s8lH3vy_YX0T7f27yXQ9vZkXwJWrGu7ttrMs3BgOQmPfjBKCE5BOgIcdJumkDPaAlfeReMMADXYq2gEBn-FVqr1-ow-H2n_YiMMknP--wfR3FrP:1qHLGH:NUHZaGApFbv-2rVwiiYJqpN0f1XAQC2L-b-vJRsCZRY; sessionid=.eJxVj81uxCAMhN-F8yYCYv5y7L3PEJlgEroRrEIi9Ud995JqL3vwwTOfZ-QfdqbARqYNASgVuzlG04GVqrPSmM4rFFGRDkCO3VjZF8zpG49U8vS4s1Hc2Ib1mLaypNxWbS3AoI3rtXZykM2f8DzW6ay0T_9Vgr1oHuc75csIH5iX0s8lH3vy_YX0T7f27yXQ9vZkXwJWrGu7ttrMs3BgOQmPfjBKCE5BOgIcdJumkDPaAlfeReMMADXYq2gEBn-FVqr1-ow-H2n_YiMMknP--wfR3FrP:1qHLWw:UnAi1zWcSezaYLaQ1RDQ8ZwobQ36Pbd7LR1ynVk2Aao',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'Content-Type': 'application/json'
}
project=3

def getImg_info(id):
    url = f"http://127.0.0.1:8080/api/tasks/{id}?project={project}"
    res = requests.request("GET", url, headers=headers)
    return res

def delete_draft(drafts_id):
    url = f"http://127.0.0.1:8080/api/drafts/{drafts_id}?project={project}"
    res = requests.request("DELETE", url, headers=headers)
    return res

def delete_ann(id, ann_id):
    url = f"http://127.0.0.1:8080/api/annotations/{ann_id}?taskID={id}&project={project}"
    res = requests.request("DELETE", url, headers=headers)
    return res

def add_ann(id, result_ls, drafts_id=0):
    url = f"http://127.0.0.1:8080/api/tasks/{id}/drafts?project={project}"
    payload = json.dumps({
        "lead_time": 10,
        "result": result_ls,
        "draft_id": drafts_id,
        "parent_prediction": None,
        "parent_annotation": None,
        "project": project
    })

    res = requests.request("POST", url, headers=headers, data=payload)
    return res
