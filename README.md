# Rust Crate String Extractor - Ghidra

Extracts string references to Rust crates in compiled Rust programs.

## Example
![usage_example.png](https://github.com/BinaryDefense/GhidraRustDependenciesExtractor/blob/main/img/usage_example.png)

## Installation Guide
Download the `RustDependencyStrings.py` file and place it into the `~/ghidra_scripts` directory.

```bash
mkdir ~/ghidra_scripts
curl -L "https://raw.githubusercontent.com/BinaryDefense/GhidraRustDependenciesExtractor/main/RustDependencyStrings.py" -o ~/ghidra_scripts/RustDependencyStrings.py
```

Run Ghidra and click on the green dragon CodeBrowser icon in the Tool Chest.

![ghidra_splash.png](https://github.com/BinaryDefense/GhidraRustDependenciesExtractor/blob/main/img/ghidra_splash.png)

Open the Script Manager window by selecting `Window -> Script Manager` in the application menu.

![ghidra_script_manager_context.png](https://github.com/BinaryDefense/GhidraRustDependenciesExtractor/blob/main/img/ghidra_script_manager_context.png) 

Select the `Manage Script Directories` button in the top right corner of the script manager window.

![ghidra_script_directory.png](https://github.com/BinaryDefense/GhidraRustDependenciesExtractor/blob/main/img/ghidra_script_directory_menu.png)

Add the `~/ghidra_scripts` directory as a bundle.

![ghidra_bundle_directory_menu.png](https://github.com/BinaryDefense/GhidraRustDependenciesExtractor/blob/main/img/ghidra_bundle_directory_menu.png)

![select_bundles.png](https://github.com/BinaryDefense/GhidraRustDependenciesExtractor/blob/main/img/select_bundles.png)

Click `Ok` and the `~/ghidra_scripts` directory should be added as a script search directory for Ghidra indicated by a green path location and check mark.

![bungle_manager.png](https://github.com/BinaryDefense/GhidraRustDependenciesExtractor/blob/main/img/bundle_manager.png)

Exit out of the bundle manager and refresh the script list.

![script_list_refresh.png](https://github.com/BinaryDefense/GhidraRustDependenciesExtractor/blob/main/img/script_list_refresh.png)

Ensure the script `RustDependencyStrings.py` is available in the list.

![script_manager.png](https://github.com/BinaryDefense/GhidraRustDependenciesExtractor/blob/main/img/script_manager.png)

The script is now loaded and can be ran by opening a Rust binary, navigating to the `Script Manager` window, and double-clicking on the `RustDependencyStrings.py` script.