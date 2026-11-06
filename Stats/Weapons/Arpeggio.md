# Arpeggio

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Medium · **Game ID:** `AssaultRifle_Burst_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/DA_Item_AssaultRifle_Burst_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Projectile_AssaultRifle_Burst_01.json) · [BP_Item_AssaultRifle_Base](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 9.5 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 1× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 1100 |
| RPM interval (s) | 0.0545 |
| Magazine | 24 |
| Reload stat (s) | 4 |
| Cooldown (s) | 0.5 |
| Firing mode | Burst |
| Shots per burst | 3 |
| ARC armor propagation multiplier | 0.4× |
| Durability burn rate | 0.001378 |
| Partial-reload base duration (s) | 2.5 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Cooldown (s) | Durability burn rate |
| --- | --- | --- | --- |
| II | −0.5 | −0.1 | −0.000138 |
| III | −1 | −0.2 | −0.000276 |
| IV | −1.5 | −0.3 | −0.000413 |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 9.5 |
| Armor | 3.8 |
| Sturdy | 3.8 |
| WeakPoint | 14.25 |
| Critical | 14.25 |
| Fragile | 11.4 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 15 | 1.001× | Linear |
| 150 | 1.001× | Linear |
| 170 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/Curve_DamageFalloff_AssaultRifle_Burst_01.json)
