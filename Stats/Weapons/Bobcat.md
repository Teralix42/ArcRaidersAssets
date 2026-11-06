# Bobcat

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Light · **Game ID:** `SMG_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/DA_Item_SMG_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/BP_Projectile_SMG_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 6 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 0.2× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 1000 |
| RPM interval (s) | 0.06 |
| Magazine | 20 |
| Reload stat (s) | 3.5 |
| Firing mode | Full-auto |
| ARC armor propagation multiplier | 0.1× |
| Durability burn rate | 0.000671 |
| Partial-reload base duration (s) | 2.18 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Durability burn rate | Handling modifiers |
| --- | --- | --- | --- |
| II | −0.5 | −6.7e−05 | −11.538462% horizontal recoil, −13.043478% max firing dispersion |
| III | −1 | −0.000134 | −23.076923% horizontal recoil, −26.086957% max firing dispersion |
| IV | −1.5 | −0.000201 | −34.615385% horizontal recoil, −39.130435% max firing dispersion |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 6 |
| Armor | 0.48 |
| Sturdy | 2.4 |
| WeakPoint | 9 |
| Critical | 9 |
| Fragile | 7.2 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 130 | 1.001× | Linear |
| 150 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/Curve_DamageFalloff_SMG_01.json)
