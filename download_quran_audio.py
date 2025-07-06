
import os
import requests

# === Customize Reciter and Save Folder ===
reciter = "bandar_baleela"
save_folder = f"MyQuranDownloads/{reciter}"
os.makedirs(save_folder, exist_ok=True) 

#absolute path in windows = save_folder = "C:\\Users\\ahmed\\Downloads\\Quran\\sa3ood_al-shuraym"

# === Loop Through All Surahs (001 to 114) ===
for i in range(1, 115):
    surah_number = f"{i:03}"  # Format number as 3 digits
    url = f"https://download.quranicaudio.com/quran/{reciter}/complete/{surah_number}.mp3"
    filepath = os.path.join(save_folder, f"{surah_number}.mp3")

    try:
        print(f"Downloading Surah {surah_number} ...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download Surah {surah_number} — Status: {response.status_code}")
    except Exception as e:
        print(f"Error downloading Surah {surah_number}: {e}")
