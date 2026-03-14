"""Scheduled LinkedIn post — Option 2 (27-seconds hook with E83 image)."""

import subprocess
import requests
import time
import sys
from datetime import datetime, timedelta

def get_key(s):
    return subprocess.run(['security','find-generic-password','-a','stikman28','-s',s,'-w'], capture_output=True, text=True).stdout.strip()

POST_TEXT = """27 seconds.

That's how fast an attacker moved from initial access to lateral movement in 2025. Not a typo. Twenty-seven seconds.

We just finished analyzing our third major annual threat report in three weeks — CrowdStrike following Unit 42 and Cloudflare.

The convergence is the story. Three vendors, independently confirming the same shifts:

→ 90% of incidents involve identity compromise
→ 82% of intrusions are malware-free
→ The largest theft in history ($1.46B) was a supply chain attack

Your antivirus can't catch what isn't malware. Your perimeter can't stop someone who already has valid credentials.

Full E83 breakdown below — free, no gates.

#cybersecurity #threatintelligence"""

IMAGE_PATH = "/Users/stikman/Projects/ai-assistant/fir-risk-intelligence/newsletters/images/e83-crowdstrike-global-threat-report.png"

def post():
    access_token = get_key('LINKEDIN_ACCESS_TOKEN')
    person_id = get_key('LINKEDIN_PERSON_ID')
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Linkedin-Version': '202503',
        'X-Restli-Protocol-Version': '2.0.0',
        'Content-Type': 'application/json',
    }

    # Upload image
    print(f'[{datetime.now():%H:%M:%S}] Uploading E83 image...')
    init = requests.post('https://api.linkedin.com/rest/images?action=initializeUpload', headers=headers, json={
        'initializeUploadRequest': {'owner': f'urn:li:person:{person_id}'}
    })
    if init.status_code != 200:
        print(f'Image init failed: {init.status_code} {init.text}')
        return False
    
    upload_url = init.json()['value']['uploadUrl']
    image_urn = init.json()['value']['image']
    
    with open(IMAGE_PATH, 'rb') as f:
        requests.put(upload_url, data=f.read(), headers={
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/octet-stream',
        })
    print(f'Image uploaded: {image_urn}')

    # Create post
    print('Posting to LinkedIn...')
    resp = requests.post('https://api.linkedin.com/rest/posts', headers=headers, json={
        'author': f'urn:li:person:{person_id}',
        'commentary': POST_TEXT,
        'visibility': 'PUBLIC',
        'distribution': {'feedDistribution': 'MAIN_FEED', 'targetEntities': [], 'thirdPartyDistributionChannels': []},
        'content': {'media': {'id': image_urn}},
        'lifecycleState': 'PUBLISHED',
        'isReshareDisabledByAuthor': False,
    })

    if resp.status_code in (200, 201):
        post_urn = resp.headers.get('x-restli-id', 'unknown')
        print(f'Posted! URN: {post_urn}')
        return True
    else:
        print(f'Failed: {resp.status_code} {resp.text}')
        return False

if __name__ == '__main__':
    delay_min = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    target = datetime.now() + timedelta(minutes=delay_min)
    print(f'Option 2 scheduled for {target:%H:%M:%S} ({delay_min} min from now)')
    print(f'Post: "27 seconds..." with E83 image')
    print(f'Leave this terminal open. Ctrl+C to cancel.\n')
    
    time.sleep(delay_min * 60)
    
    print(f'[{datetime.now():%H:%M:%S}] Executing scheduled post...')
    if post():
        print('Done! Check your LinkedIn feed.')
        print('Remember to add the link comment manually:')
        print('  Full E83 newsletter — The Convergence: https://firrisk.ai/tuesday/e83-crowdstrike-global-threat-report/')
    else:
        print('Post failed. Try running again or post manually.')
