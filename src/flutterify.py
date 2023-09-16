import os
import subprocess


def create_directories(base_directory, directories):
    """
    Create directories and subdirectories.

    Args:
        base_directory (str): The base directory in which to create directories.
        directories (list): A list of directory names to create.

    Returns:
        None
    """
    for directory in directories:
        directory_path = os.path.join(base_directory, directory)
        os.makedirs(directory_path, exist_ok=True)


def create_dart_file(directory, file_name, content=""):
    """
    Create a Dart file with the specified content.

    Args:
        directory (str): The directory where the Dart file will be created.
        file_name (str): The name of the Dart file.
        content (str): The content to write into the Dart file.

    Returns:
        None
    """
    file_path = os.path.join(directory, file_name)
    with open(file_path, "w") as file:
        file.write(content)


def open_in_android_studio(project_directory):
    try:
        subprocess.run(["studio", project_directory])
    except FileNotFoundError:
        print("Android Studio not found. Please make sure it is installed and in your system PATH.")
        suggestion = "export PATH=$PATH:/Applications/Android\\ Studio.app/Contents/bin"
        print(f"You can add Android Studio to your PATH by running the following command:\n{suggestion}")


def open_in_vscode(project_directory):
    try:
        subprocess.run(["code", project_directory])
    except FileNotFoundError:
        print("Visual Studio Code not found. Please make sure it is installed and in your system PATH.")


def clear_screen():
    os.environ['TERM'] = 'xterm'

    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    while True:
        project_name = input("Enter Flutter project name: ")
        package_name = input("Enter package name (or press Enter to use com.anon007 as default): ").strip()
        if not package_name:
            package_name = "com.anon007"

        formatted_project_name = project_name.lower()

        home_directory = os.path.expanduser("~")
        studio_projects_directory = os.path.join(home_directory, "StudioProjects")
        project_directory = os.path.join(studio_projects_directory, formatted_project_name)

        if os.path.exists(project_directory):
            print(f'Error: The project "{project_directory}" already exists. Please choose a different name.')
        else:
            break

    if not os.path.exists(studio_projects_directory):
        os.mkdir(studio_projects_directory)

    # Change into the StudioProjects directory
    os.chdir(studio_projects_directory)

    # Create the Flutter project with the specified package name
    os.system(f'flutter create --org {package_name} {formatted_project_name}')

    # Specify the directories to create within the project
    directories_to_create = [
        os.path.join(project_directory, "assets"),
        os.path.join(project_directory, "assets", "icons"),
        os.path.join(project_directory, "assets", "images"),
        os.path.join(project_directory, "assets", "fonts"),
        os.path.join(project_directory, 'lib', 'widgets'),
        os.path.join(project_directory, 'lib', 'config'),
        os.path.join(project_directory, 'lib', 'view'),
        os.path.join(project_directory, 'lib', 'viewmodels'),
        os.path.join(project_directory, 'lib', 'services'),
        os.path.join(project_directory, 'lib', 'config', 'constants'),
        os.path.join(project_directory, 'lib', 'config', 'res', 'assets'),
        os.path.join(project_directory, 'lib', 'config', 'res', 'routes'),
        os.path.join(project_directory, 'lib', 'config', 'res', 'strings'),
        os.path.join(project_directory, 'lib', 'config', 'themes')
    ]

    create_directories(project_directory, directories_to_create)

    # Create Dart files in specific directories
    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'constants'), 'app_const.dart')
    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'constants'), 'size_config.dart')

    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'res', 'assets'), 'app_icons.dart')
    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'res', 'assets'), 'app_images.dart')

    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'res', 'routes'), 'app_routes.dart')
    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'res', 'routes'), 'route_paths.dart')
    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'res', 'routes'), 'routes.dart')

    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'res', 'strings'), 'app_strings.dart')

    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'themes'), 'app_colors.dart')
    create_dart_file(os.path.join(project_directory, 'lib', 'config', 'themes'), 'app_themes.dart')

    create_dart_file(os.path.join(project_directory, 'lib'), 'config.dart')

    # Change into the project directory
    os.chdir(os.path.join(project_directory, 'lib'))

    clear_screen()

    print(f'Flutter project "{formatted_project_name}" created.')

    while True:
        choice = input(
            "Do you want to open the project in Android Studio (A), Visual Studio Code (V), open the project "
            "directory (D), or cancel (C)? ").strip().lower()
        if choice == 'a':
            open_in_android_studio(project_directory)
            break
        elif choice == 'v' or choice == '':
            open_in_vscode(project_directory)
            break
        elif choice == 'd':
            # Open the project directory
            subprocess.run(["open", project_directory])
        elif choice == 'c':
            print("Process canceled. The project was created but not opened.")
            break
        else:
            print("Invalid choice. Please enter 'A' for Android Studio, 'V' for Visual Studio Code, 'D' to open the "
                  "project directory, or 'C' to cancel.")

    print(f'Flutter project "{formatted_project_name}" created.')
