# Bantam

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Heavy · **Game ID:** `HandCannon_DoubleAction_Snubnose_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Item_HandCannon_DoubleAction_Snubnose_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/DA_Item_HandCannon_DoubleAction_Snubnose_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_WeaponQualitySet_HandCannon_DoubleAction_Snubnose_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/BP_Projectile_HandCannon_DoubleAction_Snubnose_01.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 24 |
| Headshot multiplier | 1.5× |
| ARC armor multiplier | 1.5× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 300 |
| RPM interval (s) | 0.2 |
| Magazine | 8 |
| Hipfire trigger delay (s) | 0.06 |
| ADS trigger delay (s) | 0.2 |
| ADS settling delay (s) | 0.25 |
| Input-buffer window (s) | 0.15 |
| Reload stat (s) | 3.4 |
| Firing mode | Semi-auto |
| ARC armor propagation multiplier | 1× |
| Durability burn rate | 0.001 |
| Partial-reload base duration (s) | 1.9 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Durability burn rate | Handling modifiers |
| --- | --- | --- | --- |
| II | −0.5 | −0.0001 | −13.043478% dispersion gained per shot, −0.2 dispersion recovery speed |
| III | −1 | −0.0002 | −26.086957% dispersion gained per shot, −0.4 dispersion recovery speed |
| IV | −1.5 | −0.0003 | −39.130435% dispersion gained per shot, −0.6 dispersion recovery speed |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 24 |
| Armor | 14.4 |
| Sturdy | 9.6 |
| WeakPoint | 36 |
| Critical | 36 |
| Fragile | 28.8 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 180 | 1.001× | Linear |
| 200 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/HandCannon_DoubleAction_Snubnose_01/Curve_DamageFalloff_HandCannon_DoubleAction_Snubnose_01.json)
