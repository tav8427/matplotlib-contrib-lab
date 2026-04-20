"""Short title describing your example.

One to three sentences describing what this example demonstrates
and why it is useful for engineers.
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Your plotting code here (15-30 lines) ---
# Use plt.subplots(), ax.plot(), ax.set(), etc.
# Generate data with numpy (linspace, random, exp, sin, etc.)
"""Diode I-V characteristic example.

This example demonstrates the Shockley diode equation by plotting a
silicon diode current-voltage curve. It shows how the diode current
grows exponentially in forward bias while remaining very small in
reverse bias, which is useful for understanding diode behavior in
electrical circuits.
"""

import matplotlib.pyplot as plt
import numpy as np

v = np.linspace(-0.2, 0.8, 300)
isat = 1e-12
n = 1.7
vt = 25.85e-3
i = isat * (np.exp(v / (n * vt)) - 1.0)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(v, i * 1e3, color="tab:red", label="Diode I-V")
ax.set(
    title="Silicon Diode I-V Characteristic",
    xlabel="Voltage (V)",
    ylabel="Current (mA)",
)
ax.grid(True, which="both", linestyle="--", alpha=0.6)
ax.legend()
plt.show()
