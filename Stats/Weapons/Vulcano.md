# Vulcano

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Shotgun · **Game ID:** `Shotgun_SemiAuto_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/DA_Item_Shotgun_SemiAuto_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Projectile_Shotgun_SemiAuto_01.json)

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 5.5 |
| Headshot multiplier | 1× |
| ARC armor multiplier | 0.5× |
| ARC weak-point multiplier | 1× |
| Fire rate (RPM) | 126 |
| Magazine | 6 |
| Reload stat (s) | 3.5 |
| Firing mode | Semi-auto |
| Projectiles per shot | 9 |
| Damage if all projectiles hit | 49.5 |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.005563 |
| Partial-reload base duration (s) | 2.8 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Fire rate (RPM) | Reload stat (s) | Durability burn rate |
| --- | --- | --- | --- |
| II | +14 | −0.5 | −0.000556 |
| III | +28 | −1 | −0.001113 |
| IV | +42 | −1.5 | −0.001669 |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 5.5 |
| Armor | 1.1 |
| Sturdy | 2.2 |
| WeakPoint | 8.25 |
| Critical | 8.25 |
| Fragile | 6.6 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 20 | 1.001× | Linear |
| 50 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/Curve_DamageFalloff_Shotgun_SemiAuto_01.json)
