"""Эмулятор командной строки UNIX-подобной ОС.

Этап 1. REPL с заглушками команд ls, cd и exit.
"""

import sys


class ShellEmulator:
    """Эмулятор командной строки. Реализует цикл REPL."""

    def __init__(self, vfs_name: str = "VFS") -> None:
        """Создать эмулятор.

        Args:
            vfs_name: имя виртуальной файловой системы,
                отображаемое в приглашении к вводу.
        """
        self.vfs_name = vfs_name
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

    def run(self) -> None:
        """Запустить цикл REPL."""
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


def main() -> int:
    """Точка входа в приложение."""
    emulator = ShellEmulator(vfs_name="VFS")
    emulator.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
