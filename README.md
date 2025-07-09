# 🧬 Family Tree Recursion Assignment

This is a simple Python exercise to practice recursion using a nested dictionary that represents a family tree. The goal is to complete the `get_all_children_names` function, which recursively collects all names of children and their descendants.

---

## 📂 Project Structure

```python
person = {
    "name": "John",
    "children": [
        {
            "name": "Jim",
            "children": [
                {"name": "Liam", "children": []},
                {"name": "Ella", "children": []}
            ]
        },
        {
            "name": "Zoe",
            "children": []
        }
    ]
}
