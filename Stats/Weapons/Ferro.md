# Ferro

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Heavy · **Game ID:** `BattleRifle_BreachAction_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/DA_Item_BattleRifle_BreachAction_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Projectile_BattleRifle_BreachAction_01.json) · [BP_Item_BattleRifle_Base](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json)

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 40 |
| Headshot multiplier | 2.5× |
| ARC armor multiplier | 1.5× |
| ARC weak-point multiplier | 1× |
| Fire rate (RPM) | 50 |
| Magazine | 1 |
| Reload stat (s) | 2.875 |
| Firing mode | Semi-auto |
| ARC armor propagation multiplier | 1× |
| Durability burn rate | 0.006611 |
| Partial-reload base duration (s) | 1.75 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Durability burn rate |
| --- | --- | --- |
| II | −0.375 | −0.000661 |
| III | −0.75 | −0.001322 |
| IV | −1.125 | −0.001983 |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 40 |
| Armor | 24 |
| Sturdy | 16 |
| WeakPoint | 60 |
| Critical | 60 |
| Fragile | 48 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 180 | 1.001× | Linear |
| 200 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/Curve_DamageFalloff_BattleRifle_BreachAction_01.json)
