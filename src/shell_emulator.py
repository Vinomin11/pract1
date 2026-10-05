"""Эмулятор командной строки UNIX-подобной ОС.

Этап 2. Конфигурация: аргументы командной строки и стартовый скрипт.
"""

import argparse
import sys


class ShellEmulator:
    """Эмулятор командной строки. Реализует цикл REPL."""

    def __init__(
        self,
        vfs_name: str = "VFS",
        vfs_path: str | None = None,
        script_path: str | None = None,
    ) -> None:
        """Создать эмулятор.

        Args:
            vfs_name: имя VFS для приглашения.
            vfs_path: путь к файлу VFS.
            script_path: путь к стартовому скрипту.
        """
        self.vfs_name = vfs_name
        self.vfs_path = vfs_path
        self.script_path = script_path
        self.running = True

    def get_prompt(self) -> str:
        """Сформировать приглашение к вводу с именем VFS."""
        return f"{self.vfs_name}:~$ "

    @staticmethod
    def parse_command(line: str) -> tuple[str, list[str]]:
        """Разобрать строку на команду и аргументы по пробелам."""
        parts = line.strip().split()
        if not parts:
            return "", []
        return parts[0], parts[1:]

    def dump_config(self) -> None:
        """Вывести отладочную информацию о параметрах запуска."""
        print("=== Параметры эмулятора ===")
        print(f"vfs_name    = {self.vfs_name!r}")
        print(f"vfs_path    = {self.vfs_path!r}")
        print(f"script_path = {self.script_path!r}")
        print("===========================")

    def execute(self, command: str, args: list[str]) -> str:
        """Выполнить команду и вернуть строку с результатом."""
        if command == "ls":
            return f"Заглушка ls. Аргументы: {args}"
        if command == "cd":
            return f"Заглушка cd. Аргументы: {args}"
        if command == "exit":
            self.running = False
            return "Выход из эмулятора."
        if not command:
            return ""
        return f"Ошибка: неизвестная команда '{command}'"

    def run_script(self, path: str) -> None:
        """Выполнить команды из стартового скрипта.

        Ошибочные строки пропускаются, выполнение продолжается.
        На экран выводится имитация диалога: приглашение + команда
        + результат.
        """
        try:
            with open(path, "r", encoding="utf-8") as handle:
                lines = handle.readlines()
        except FileNotFoundError:
            print(f"Ошибка: стартовый скрипт '{path}' не найден.")
            return

        for raw in lines:
            line = raw.rstrip("\n")
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            print(f"{self.get_prompt()}{line}")
            command, args = self.parse_command(line)
            result = self.execute(command, args)
            if result:
                print(result)
            if not self.running:
                break

    def run(self) -> None:
        """Запустить цикл REPL."""
        self.dump_config()
        if self.script_path:
            print(f"Выполняется стартовый скрипт: {self.script_path}")
            self.run_script(self.script_path)
            if not self.running:
                return
        print(f"Добро пожаловать в эмулятор оболочки ({self.vfs_name}).")
        print("Введите 'exit' для выхода.")
        while self.running:
            try:
                line = input(self.get_prompt())
            except (EOFError, KeyboardInterrupt):
                print()
                break
            command, args = self.parse_command(line)
            result = self.execute(command, args)
            if result:
                print(result)


def build_arg_parser() -> argparse.ArgumentParser:
    """Собрать парсер аргументов командной строки."""
    parser = argparse.ArgumentParser(
        prog="shell_emulator",
        description="Эмулятор командной строки UNIX-подобной ОС.",
    )
    parser.add_argument(
        "--vfs-path",
        dest="vfs_path",
        default=None,
        help="Путь к файлу виртуальной файловой системы.",
    )
    parser.add_argument(
        "--script-path",
        dest="script_path",
        default=None,
        help="Путь к стартовому скрипту с командами.",
    )
    return parser


def main() -> int:
    """Точка входа в приложение."""
    args = build_arg_parser().parse_args()
    emulator = ShellEmulator(
        vfs_name="VFS",
        vfs_path=args.vfs_path,
        script_path=args.script_path,
    )
    emulator.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
