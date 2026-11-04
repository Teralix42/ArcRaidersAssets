# ARC damage and resistance

[ARC stats](README.md) · [Complete model JSON](damage_model.json)

| Group | Physical resistance | Physical × | Fire × | Explosive ×, flag off | Explosive ×, flag on |
| --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 2 | 1.6 |
| Armor | 0.6 | 0.4 | 0.4 | 0.8 | 1.216 |
| Sturdy | 0.6 | 0.4 | 0.4 | 0.8 | 1.216 |
| WeakPoint | -0.5 | 1.5 | 1.5 | 3 | 1.92 |
| Critical | -0.5 | 1.5 | 1.5 | 3 | 1.92 |
| Fragile | -0.2 | 1.2 | 1.2 | 2.4 | 1.728 |

These factors apply to direct part damage before damage passes to other parts or the frame. Multiply the Armor factor by the weapon’s ARC armor multiplier and cap the result at 1×. WeakPoint and Critical use the weapon’s ARC weak-point multiplier. Both explosive settings are listed because the active flag is unknown.

The script cache used for these calculations matches Steam changelist `1438640`. [Script evidence](../Sources/NativeScript/)
