import os
import plistlib
import uuid
import zipfile

def create_font_profile(font_folder, output_profile_path, profile_name, organization, description):
    """
    Generates an iOS font profile (.mobileconfig) from a folder of .ttf fonts.

    Args:
        font_folder (str): Path to the folder containing .ttf font files.
        output_profile_path (str): Path to save the generated .mobileconfig file.
        profile_name (str): Name of the profile (displayed on iOS).
    """

    font_payloads = []
    for filename in os.listdir(font_folder):
        if filename.lower().endswith(".ttf"):
            font_path = os.path.join(font_folder, filename)
            with open(font_path, "rb") as font_file:
                font_data = font_file.read()

            font_payload = {
                "PayloadType": "com.apple.font",
                "PayloadVersion": 1,
                "PayloadIdentifier": str(uuid.uuid4()),
                "PayloadUUID": str(uuid.uuid4()),
                "PayloadDisplayName": filename,
                "Font": font_data,
            }
            font_payloads.append(font_payload)

    profile_uuid = str(uuid.uuid4())
    profile_data = {
        "PayloadContent": font_payloads,
        "PayloadDisplayName": profile_name,
        "PayloadIdentifier": "com.example.fontprofile." + profile_uuid,
        "PayloadOrganization": organization,
        "PayloadType": "Configuration",
        "PayloadUUID": profile_uuid,
        "PayloadVersion": 1,
        "PayloadDescription": description,
    }

    try:
        with open(output_profile_path, "wb") as profile_file:
            plistlib.dump(profile_data, profile_file)
        print(f"Font profile created successfully: {output_profile_path}")

    except Exception as e:
        print(f"Error creating font profile: {e}")

def zip_mobileconfig(mobileconfig_path):
    """
    Zips the .mobileconfig file.

    Args:
        mobileconfig_path (str): Path to the .mobileconfig file.
    """
    zip_path = mobileconfig_path + ".zip"
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(mobileconfig_path, os.path.basename(mobileconfig_path))
        print(f"Zipped mobileconfig to: {zip_path}")
    except Exception as e:
        print(f"Error zipping mobileconfig: {e}")

if __name__ == "__main__":

    # ADJUST THESE VARIABLES
    font_folder = "path/to/your/font/folder"  # Path to the folder containing .ttf fonts
    output_profile_path = "example.mobileconfig" # Path to save the generated .mobileconfig file
    profile_name = "Example Profile" # Name of the profile
    organization = "Example Organization" # Organization name
    description = "This is the description of the profile" # Description of the profile

    if not os.path.exists(font_folder):
        print(f"Error: Font folder '{font_folder}' not found.")
    else:
        create_font_profile(font_folder, output_profile_path, profile_name, organization, description)
        if os.path.exists(output_profile_path):
            zip_mobileconfig(output_profile_path)