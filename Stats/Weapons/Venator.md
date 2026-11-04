# Venator

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Medium · **Game ID:** `Pistol_HighPower_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Item_Pistol_HighPower_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/DA_Item_Pistol_HighPower_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_WeaponQualitySet_Pistol_HighPower_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/BP_Projectile_Pistol_HighPower_01.json)

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 8 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 0.8× |
| ARC weak-point multiplier | 1× |
| Fire rate (RPM) | 225 |
| Magazine | 10 |
| Reload stat (s) | 3.5 |
| Firing mode | Semi-auto |
| Projectiles per shot | 2 |
| Damage if all projectiles hit | 16 |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.001378 |
| Partial-reload base duration (s) | 2.5 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Fire rate (RPM) | Reload stat (s) | Durability burn rate |
| --- | --- | --- | --- |
| II | +30 | −0.5 | −0.000138 |
| III | +60 | −1 | −0.000276 |
| IV | +90 | −1.5 | −0.000413 |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 8 |
| Armor | 2.56 |
| Sturdy | 3.2 |
| WeakPoint | 12 |
| Critical | 12 |
| Fragile | 9.6 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 5 | 1.001× | Linear |
| 15 | 1.001× | Linear |
| 150 | 1.001× | Linear |
| 170 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Pistol_HighPower_01/Curve_DamageFalloff_Pistol_HighPower_01.json)
