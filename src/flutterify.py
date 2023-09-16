import os
import subprocess


class CodeSnippets:
    def __init__(self):
        self.size_config_code = """
import 'package:flutter/widgets.dart';

class SizeConfig {
  static late Size _mediaQueryData;
  static late double screenWidth;
  static late double screenHeight;
  static late double blockSizeHorizontal;
  static late double blockSizeVertical;

  static late double textMultiplier;
  static late double imageSizeMultiplier;
  static late double heightMultiplier;

  static double get screenWidthInfinity =>
      double.infinity / blockSizeHorizontal;

  static double get screenHeightInfinity => double.infinity / blockSizeVertical;

  void init(BuildContext context) {
    _mediaQueryData = MediaQuery.sizeOf(context);
    screenWidth = _mediaQueryData.width;
    screenHeight = _mediaQueryData.height;
    blockSizeHorizontal = screenWidth / 100;
    blockSizeVertical = screenHeight / 100;

    textMultiplier = blockSizeVertical;
    imageSizeMultiplier = blockSizeHorizontal;
    heightMultiplier = blockSizeVertical;
  }
}
        """

        self.app_icons_code = """
class AppIcons {
  static const placeholder = 'assets/icons/placeholder.svg';
}
        """
        self.app_images_code = """
class AppImages {
  static const placeholder = 'assets/images/placeholder.png';
}

        """
        self.route_paths = """
class RoutePaths {
  static const splashPage = '/';
  static const homePage = '/homePage';
}
        """
        self.app_themes = """
import 'package:flutter/material.dart';

class AppThemes {
  AppThemes._();

  static ThemeData lightTheme(BuildContext context) => ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: Colors.black,
      );

  static ThemeData darkTheme(BuildContext context) =>
      ThemeData.dark().copyWith();
}
        """
        self.config_code = """
export 'res/assets/app_icons.dart';
export 'res/assets/app_images.dart';
export 'res/routes/routes.dart';
export 'res/strings/app_strings.dart';
export 'themes/app_colors.dart';
export 'themes/app_themes.dart';
        """


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


def insert_code_into_file(file_path, code_to_insert):
    with open(file_path, 'a') as file:
        file.write(code_to_insert)


def main():
    code_snippets = CodeSnippets()

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

    # Architecture selection
    while True:
        architecture_choice = input(
            "Choose an architecture (Flutterify Special (1), MVVC (2), MVC (3)): ").strip()
        if architecture_choice == '1' or architecture_choice == '':

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
                os.path.join(project_directory, 'lib', 'views'),
                os.path.join(project_directory, 'lib', 'view_models'),
                os.path.join(project_directory, 'lib', 'models'),
                os.path.join(project_directory, 'lib', 'repository'),
                os.path.join(project_directory, 'lib', 'data', 'network'),
                os.path.join(project_directory, 'lib', 'data', 'response'),
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
            create_dart_file(os.path.join(project_directory, 'lib', 'config'), 'config.dart')

            create_dart_file(os.path.join(project_directory, 'lib'), 'app.dart')

            create_dart_file(os.path.join(project_directory, 'lib', 'views'), 'views.dart')
            create_dart_file(os.path.join(project_directory, 'lib', 'view_models'), 'view_models.dart')
            create_dart_file(os.path.join(project_directory, 'lib', 'models'), 'models.dart')
            create_dart_file(os.path.join(project_directory, 'lib', 'widgets'), 'widgets.dart')

            create_dart_file(os.path.join(project_directory, 'lib', 'views'), 'home_view.dart')
            create_dart_file(os.path.join(project_directory, 'lib', 'view_models'), 'home_viewmodel.dart')

            create_dart_file(os.path.join(project_directory, 'lib', 'data'), 'app_exceptions.dart')
            create_dart_file(os.path.join(project_directory, 'lib', 'data', 'network'), 'base_api_services.dart')
            create_dart_file(os.path.join(project_directory, 'lib', 'data', 'network'), 'network_api_services.dart')
            create_dart_file(os.path.join(project_directory, 'lib', 'data', 'response'), 'api_response.dart')
            create_dart_file(os.path.join(project_directory, 'lib', 'data', 'response'), 'status.dart')

            insert_code_into_file(os.path.join(project_directory, 'lib', 'config', 'constants', 'size_config.dart'),
                                  code_snippets.size_config_code)
            insert_code_into_file(os.path.join(project_directory, 'lib', 'config', 'config.dart'),
                                  code_snippets.config_code)
            insert_code_into_file(os.path.join(project_directory, 'lib', 'config', 'res', 'assets', 'app_icons.dart'),
                                  code_snippets.app_icons_code)
            insert_code_into_file(os.path.join(project_directory, 'lib', 'config', 'res', 'assets', 'app_images.dart'),
                                  code_snippets.app_images_code)
            insert_code_into_file(os.path.join(project_directory, 'lib', 'config', 'res', 'routes', 'route_paths.dart'),
                                  code_snippets.route_paths)
            insert_code_into_file(os.path.join(project_directory, 'lib', 'config', 'themes', 'app_themes.dart'),
                                  code_snippets.app_themes)

            break
        elif architecture_choice == '2':
            print("MVVC architecture is under construction. Please wait for an update.")
            break
        elif architecture_choice == '3':
            print("MVC architecture is under construction. Please wait for an update.")
            break
        else:
            print("Invalid choice. Please enter '1' for Flutterify Special, '2' for MVVC, '3' for MVC, or press Enter "
                  "for Flutterify Special (default).")

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


if __name__ == '__main__':
    main()
