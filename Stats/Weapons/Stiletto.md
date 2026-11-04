# Stiletto

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Light · **Game ID:** `BattleRifle_SemiAuto_Light_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/DA_Item_BattleRifle_SemiAuto_Light_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Projectile_BattleRifle_SemiAuto_Light_01.json)

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 19 |
| Headshot multiplier | 1.8× |
| ARC armor multiplier | 0.4× |
| ARC weak-point multiplier | 1× |
| Fire rate (RPM) | 175 |
| Magazine | 10 |
| Reload stat (s) | 3.13 |
| Firing mode | Semi-auto |
| ARC armor propagation multiplier | 0.2× |
| Durability burn rate | 0.001 |
| Partial-reload base duration (s) | 2.6 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Fire rate (RPM) | Magazine | Reload stat (s) | Durability burn rate |
| --- | --- | --- | --- | --- |
| II | +15 | +2 | −0.33 | −0.0001 |
| III | +30 | +4 | −0.66 | −0.0002 |
| IV | +45 | +6 | −0.99 | −0.0003 |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 19 |
| Armor | 3.04 |
| Sturdy | 7.6 |
| WeakPoint | 28.5 |
| Critical | 28.5 |
| Fragile | 22.8 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1× | Linear |
| 130 | 1.001× | Linear |
| 150 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/Curve_DamageFalloff_BattleRifle_SemiAuto_Light_01.json)
