from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def scraping_rootme(username):
    url = f'https://www.root-me.org/{username}'
    response = requests.get(url)

    if response.status_code == 404:
        return {
            "userName": "Unknown",
            "userRank": "Unknown",
            "userScore": "Unknown",
            "userChallenge": "Unknown",
            "totalChallenge": "Unknown",
            "userPercent": "Unknown"
        }

    html = response.text
    userName = username
    userRank = userScore = userChallenge = totalChallenge = userPercent = "Unknown"

    for line in html.splitlines():
        if "<h3><img src='squelettes/img/classement.svg?1647504561' width='24' height='24' />&nbsp;" in line:
            userRank = line.split("&nbsp;")[1].split("</h3>")[0].strip()
        if "<h3><img src='squelettes/img/valid.svg?1566650916' width='24' height='24' />&nbsp;" in line:
            userScore = line.split("&nbsp;")[1].split("</h3>")[0].strip()
        if "<h3><img src='IMG/logo/rubon5.svg?1637496507' width='24' height='24' />&nbsp;" in line:
            userChallenge = line.split("&nbsp;")[1].split("</h3>")[0].strip()
        if '<span class="gris">/' in line:
            totalChallenge = line.split('<span class="gris">/')[1].split('</span>')[0].strip()
        if "<h3 class=\"text-center\">" in line:
            userPercent = line.split("<h3 class=\"text-center\">")[1].split("&nbsp;")[0].strip()
    
    return {
        "userName": userName,
        "userRank": userRank,
        "userScore": userScore,
        "userChallenge": userChallenge,
        "totalChallenge": totalChallenge,
        "userPercent": userPercent
    }

@app.route('/api', methods=['GET'])
def get_rootme_stats():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    return scraping_rootme(username)

if __name__ == '__main__':
    app.run(debug=True)
