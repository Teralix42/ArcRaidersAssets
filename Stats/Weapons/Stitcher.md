# Stitcher

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Light · **Game ID:** `SMG_LowTier_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_LowTier_01/BP_Item_SMG_LowTier_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_LowTier_01/DA_Item_SMG_LowTier_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_LowTier_01/BP_WeaponQualitySet_SMG_LowTier_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_LowTier_01/BP_Projectile_SMG_LowTier_01.json) · [BP_Item_SMG_Base](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/SMG_Base/BP_Item_SMG_Base.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Level I

| Stat | Value |
| --- | --- |
| Body damage / projectile | 6.5 |
| Headshot multiplier | 1.75× |
| ARC armor multiplier | 0.2× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 680 |
| RPM interval (s) | 0.0882 |
| Magazine | 20 |
| Reload stat (s) | 3 |
| Firing mode | Full-auto |
| ARC armor propagation multiplier | 0.1× |
| Durability burn rate | 0.001414 |
| Partial-reload base duration (s) | 2 |

### Level II–IV changes

All deltas are relative to Level I. A dash means unchanged.

| Level | Reload stat (s) | Durability burn rate | Handling modifiers |
| --- | --- | --- | --- |
| II | −0.5 | −0.000141 | −16.666667% horizontal recoil |
| III | −1 | −0.000283 | −33.333333% horizontal recoil |
| IV | −1.5 | −0.000424 | −50% horizontal recoil |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 6.5 |
| Armor | 0.52 |
| Sturdy | 2.6 |
| WeakPoint | 9.75 |
| Critical | 9.75 |
| Fragile | 7.8 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.2× | Linear |
| 5 | 1.2× | Linear |
| 15 | 1.001× | Linear |
| 130 | 1.001× | Linear |
| 150 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_LowTier_01/Curve_DamageFalloff_SMG_LowTier_01.json)
