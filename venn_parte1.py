from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# Definición de los conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 1. Unión (A | B)
plt.figure(figsize=(5,5))
venn = venn2([A, B], set_labels=("A", "B"))
venn.get_label_by_id('10').set_text("\n".join(map(str, A - B)))
venn.get_label_by_id('01').set_text("\n".join(map(str, B - A)))
venn.get_label_by_id('11').set_text("\n".join(map(str, A & B)))
plt.title(f"Unión A | B = {A | B}")
plt.show()

# 2. Intersección (A & B)
plt.figure(figsize=(5,5))
venn = venn2([A, B], set_labels=("A", "B"))
venn.get_label_by_id('10').set_text("")   # vacío
venn.get_label_by_id('01').set_text("")   # vacío
venn.get_label_by_id('11').set_text("\n".join(map(str, A & B)))
plt.title(f"Intersección A & B = {A & B}")
plt.show()

# 3. Diferencia (A - B)
plt.figure(figsize=(5,5))
venn = venn2([A, B], set_labels=("A", "B"))
venn.get_label_by_id('10').set_text("\n".join(map(str, A - B)))
venn.get_label_by_id('01').set_text("")   # vacío
venn.get_label_by_id('11').set_text("")   # vacío
plt.title(f"Diferencia A - B = {A - B}")
plt.show()

# 4. Diferencia (B - A)
plt.figure(figsize=(5,5))
venn = venn2([A, B], set_labels=("A", "B"))
venn.get_label_by_id('10').set_text("")   # vacío
venn.get_label_by_id('01').set_text("\n".join(map(str, B - A)))
venn.get_label_by_id('11').set_text("")   # vacío
plt.title(f"Diferencia B - A = {B - A}")
plt.show()

# 5. Diferencia simétrica (A ^ B)
plt.figure(figsize=(5,5))
venn = venn2([A, B], set_labels=("A", "B"))
venn.get_label_by_id('10').set_text("\n".join(map(str, A - B)))
venn.get_label_by_id('01').set_text("\n".join(map(str, B - A)))
venn.get_label_by_id('11').set_text("")   # vacío (no se incluye la intersección)
plt.title(f"Diferencia simétrica A ^ B = {A ^ B}")
plt.show()
