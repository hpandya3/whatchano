import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

def analysis(key, dictionary, emotions):

    def return_useful_results(post):

        image = post['display_src']
        image_report = get_result(key, image)

        if len(image_report) > 0:

            meets_criteria = False

            for person in image_report:
                if 'faceAttributes' in person:
                    if 'emotion' in person['faceAttributes']:
                        e_res = person['faceAttributes']['emotion']

                        if (
                            e_res['anger'] >= emotions['anger']
                            and e_res['contempt'] >= emotions['contempt']
                            and e_res['disgust'] >= emotions['disgust']
                            and e_res['fear'] >= emotions['fear']
                            and e_res['happiness'] <= e_res['happiness']
                            and e_res['neutral'] >= e_res['neutral']
                            and e_res['sadness'] >= e_res['sadness']
                            and e_res['surprise'] >= e_res['surprise']
                        ):

                            meets_criteria = True

            if meets_criteria:

                post['cognitive_analysis'] = person
                return post

        return dict()

    juicy_results = list(map(return_useful_results, dictionary))

    def remove_empty(post):
        if len(post) > 0:
            return post

    clean_results = list(filter(remove_empty, juicy_results))

    return clean_results


def get_result(key, image_url):

    uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

    # Request headers.
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key,
    }

    # Request parameters.
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    # Body. The URL of a JPEG image to analyze.
    body = {'url': image_url}

    try:
        # Execute the REST API call and get the response.
        response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)

        parsed = json.loads(response.text)
        return parsed

    except Exception as e:
        return dict()
