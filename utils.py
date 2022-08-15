def is_expected_status(response, expected_status: int):
    if 'status' in response.json():
        return response.json()['status'] == expected_status or response.status_code == expected_status
    else:
        return response.status_code == expected_status
