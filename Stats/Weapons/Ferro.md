[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Ferro

Internal weapon id: `BattleRifle_BreachAction_01`. Ammo: **HeavyAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 40 | 1 | 40 | 2.5 | 1.5 | 1 | 50 | 1 | 2.875 |
| II | 40 | 1 | 40 | 2.5 | 1.5 | 1 | 50 | 1 | 2.5 |
| III | 40 | 1 | 40 | 2.5 | 1.5 | 1 | 50 | 1 | 2.125 |
| IV | 40 | 1 | 40 | 2.5 | 1.5 | 1 | 50 | 1 | 1.75 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | BattleRifle_BreachAction_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 40 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 40 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 50 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 2.875 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.006611 |
| Base partial-reload duration, seconds | 1.75 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 40 | 40 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 24 | 24 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 16 | 16 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 48 | 48 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 40 |
| Fire rate | 1.6 |
| Range | 53.09 |
| Stability | 78.1 |
| Agility | 31.5 |
| Stealth | 8 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/Curve_DamageFalloff_BattleRifle_BreachAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.375 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/DA_Item_BattleRifle_BreachAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Projectile_BattleRifle_BreachAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | BattleRifle_BreachAction_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 40 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 40 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 50 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00595 |
| Base partial-reload duration, seconds | 1.75 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 40 | 40 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 24 | 24 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 16 | 16 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 48 | 48 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 40 |
| Fire rate | 6.6 |
| Range | 53.09 |
| Stability | 78.1 |
| Agility | 31.5 |
| Stealth | 8 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/Curve_DamageFalloff_BattleRifle_BreachAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/DA_Item_BattleRifle_BreachAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Projectile_BattleRifle_BreachAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | BattleRifle_BreachAction_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 40 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 40 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 50 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 2.125 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.005289 |
| Base partial-reload duration, seconds | 1.75 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 40 | 40 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 24 | 24 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 16 | 16 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 48 | 48 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 40 |
| Fire rate | 11.6 |
| Range | 53.09 |
| Stability | 78.1 |
| Agility | 31.5 |
| Stealth | 8 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/Curve_DamageFalloff_BattleRifle_BreachAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.375 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/DA_Item_BattleRifle_BreachAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Projectile_BattleRifle_BreachAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | BattleRifle_BreachAction_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 40 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 40 |
| Firearm critical/headshot multiplier | 2.5 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 50 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 1 |
| Reload time stat, seconds | 1.75 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.004628 |
| Base partial-reload duration, seconds | 1.75 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 40 | 40 |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 24 | 24 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 16 | 16 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 60 | 60 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 48 | 48 |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 40 |
| Fire rate | 16.6 |
| Range | 53.09 |
| Stability | 78.1 |
| Agility | 31.5 |
| Stealth | 8 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/Curve_DamageFalloff_BattleRifle_BreachAction_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 18,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 20,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.75 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/DA_Item_BattleRifle_BreachAction_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Projectile_BattleRifle_BreachAction_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json, Script/PrecompiledScript.Cache

### Amplified configurations

No definition found in this snapshot.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Item_BattleRifle_BreachAction_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Projectile_BattleRifle_BreachAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_Projectile_BattleRifle_BreachAction_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/BP_WeaponQualitySet_BattleRifle_BreachAction_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/Curve_DamageFalloff_BattleRifle_BreachAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/Curve_DamageFalloff_BattleRifle_BreachAction_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/DA_Item_BattleRifle_BreachAction_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_BreachAction_01/DA_Item_BattleRifle_BreachAction_01.json)
- [Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json)

</details>
