# iOS Font Profile Generator

This Python script generates iOS font configuration profiles (`.mobileconfig`) from a folder containing `.ttf` font files. It also zips the generated profile for easier distribution.

## Features

* Generates valid iOS font configuration profiles.
* Handles multiple `.ttf` fonts in a specified folder.
* Includes customizable profile name, organization, and description.
* Zips the generated `.mobileconfig` file for convenient distribution.
* Robust error handling.

## Prerequisites

* Python 3.x
* A folder containing your `.ttf` font files.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/bestler/Fonts_to_Profile_iOS
    cd Fonts_to_Profile_iOS
    ```

2.  **Ensure you have python installed. (if not, install it)**

## Usage

1.  **Place your `.ttf` font files in a folder.** (e.g., `fonts/`)

2.  **Edit the `main` section of `generate_profile.py`:**

    ```python
    if __name__ == "__main__":

        # ADJUST THESE VARIABLES
        font_folder = "path/to/your/font/folder"  # Path to the folder containing .ttf fonts
        output_profile_path = "example.mobileconfig" # Path to save the generated .mobileconfig file
        profile_name = "Example Profile" # Name of the profile
        organization = "Example Organization" # Organization name
        description = "This is the description of the profile" # Description of the profile

        # ... rest of the code ...
    ```

    * Replace `"path/to/your/font/folder"` with the actual path to your font folder.
    * Modify `output_profile_path`, `profile_name`, `organization`, and `description` as needed.

3.  **Run the script:**

    ```bash
    python generate_profile.py
    ```

4.  **Distribution:** The script will generate `example.mobileconfig` and `example.mobileconfig.zip` (or whatever you named your output file). Distribute the `.zip` file to iOS devices.

## Example

If you have a folder named `my_fonts` with `Roboto-Regular.ttf` and `OpenSans-Bold.ttf`, and you want to create a profile named "My Custom Fonts" for "My Company" with the description "Custom fonts for iOS," you would modify the script like this:

```python
if __name__ == "__main__":

    # ADJUST THESE VARIABLES
    font_folder = "my_fonts"
    output_profile_path = "MyFonts.mobileconfig"
    profile_name = "My Custom Fonts"
    organization = "My Company"
    description = "Custom fonts for iOS"

    # ... rest of the code ...
```

## ⚠️ Important Notes
- iOS Compatibility: Font profiles are supported on iOS 7 and later.
- Font Licensing: Always ensure you have the necessary licenses to distribute the fonts.
- Security: Distribute profiles from trusted sources.
- Testing: Test the generated profile on a test iOS device before wide distribution.
## Contributing
Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request. 
