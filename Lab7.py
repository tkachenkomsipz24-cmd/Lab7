from collections import deque
from dataclasses import dataclass

lines = [
    "",
    "a + b",
    "{[a] + (b)}",
    "([)]",
    "a)",
    "(a[b]",
    "f(x[1]) * {y + (z)}",
]


@dataclass
class Request:
    name: str
    minutes: int


requests = [
    Request("Довідка про навчання", 4),
    Request("Академічна відпустка", 7),
    Request("Копія наказу", 2),
    Request("Виписка з оцінками", 6),
    Request("Перескладання", 9),
    Request("Студентський квиток", 3),
]


def isBalanced(line: str) -> bool:
    stack = deque()
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())

    for ch in line:
        if ch in opening:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


def processQueue(requests_list: list[Request]) -> None:
    if not requests_list:
        print("Черга порожня, обробляти нічого.")
        return

    queue = deque(requests_list)
    current_time = 0
    total_wait = 0
    step = 0

    while queue:
        req = queue.popleft()
        step += 1
        start_time = current_time
        end_time = start_time + req.minutes
        total_wait += start_time
        print(f"{step}. {req.name:<22} з {start_time} до {end_time} хв")
        current_time = end_time

    avg_wait = total_wait / step
    print(f"Оброблено заявок: {step}, загальний час: {current_time} хв")
    print(f"Середній час очікування: {avg_wait:.2f} хв")


if __name__ == "__main__":
    for line in lines:
        label = "(порожній рядок)" if line == "" else line
        result = "так" if isBalanced(line) else "ні"
        print(f"{label:<25} -> {result}")

    print()
    processQueue(requests)
    print()
    processQueue([])