[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Stiletto

Internal weapon id: `BattleRifle_SemiAuto_Light_01`. Ammo: **LightAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 19 | 1 | 19 | 1.8 | 0.4 | 1 | 175 | 10 | 3.13 |
| II | 19 | 1 | 19 | 1.8 | 0.4 | 1 | 190 | 12 | 2.8 |
| III | 19 | 1 | 19 | 1.8 | 0.4 | 1 | 205 | 14 | 2.47 |
| IV | 19 | 1 | 19 | 1.8 | 0.4 | 1 | 220 | 16 | 2.14 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | BattleRifle_SemiAuto_Light_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 19 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 19 |
| Firearm critical/headshot multiplier | 1.8 |
| ARC armour multiplier | 0.4 |
| ARC armour propagation coefficient | 0.2 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 175 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 10 |
| Reload time stat, seconds | 3.13 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001 |
| Base partial-reload duration, seconds | 2.6 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 19 | 19 |
| Armor | 0.6 | 0.4 | 0.4 | 1 | 0.16 | 3.04 | 3.04 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 7.6 | 7.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 22.8 | 22.8 |

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
| Damage | 19 |
| Fire rate | 11.167 |
| Range | 51.763 |
| Stability | 75.078 |
| Agility | 66.498 |
| Stealth | 20 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/Curve_DamageFalloff_BattleRifle_SemiAuto_Light_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.33 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | -15 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/DA_Item_BattleRifle_SemiAuto_Light_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Projectile_BattleRifle_SemiAuto_Light_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | BattleRifle_SemiAuto_Light_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 19 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 19 |
| Firearm critical/headshot multiplier | 1.8 |
| ARC armour multiplier | 0.4 |
| ARC armour propagation coefficient | 0.2 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 190 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 12 |
| Reload time stat, seconds | 2.8 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.0009 |
| Base partial-reload duration, seconds | 2.6 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 19 | 19 |
| Armor | 0.6 | 0.4 | 0.4 | 1 | 0.16 | 3.04 | 3.04 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 7.6 | 7.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 22.8 | 22.8 |

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
| Damage | 19 |
| Fire rate | 12.667 |
| Range | 51.763 |
| Stability | 75.578 |
| Agility | 66.498 |
| Stealth | 20 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/Curve_DamageFalloff_BattleRifle_SemiAuto_Light_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/DA_Item_BattleRifle_SemiAuto_Light_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Projectile_BattleRifle_SemiAuto_Light_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | BattleRifle_SemiAuto_Light_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 19 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 19 |
| Firearm critical/headshot multiplier | 1.8 |
| ARC armour multiplier | 0.4 |
| ARC armour propagation coefficient | 0.2 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 205 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 14 |
| Reload time stat, seconds | 2.47 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.0008 |
| Base partial-reload duration, seconds | 2.6 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 19 | 19 |
| Armor | 0.6 | 0.4 | 0.4 | 1 | 0.16 | 3.04 | 3.04 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 7.6 | 7.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 22.8 | 22.8 |

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
| Damage | 19 |
| Fire rate | 14.167 |
| Range | 51.763 |
| Stability | 75.578 |
| Agility | 66.498 |
| Stealth | 20 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/Curve_DamageFalloff_BattleRifle_SemiAuto_Light_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.33 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 15 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/DA_Item_BattleRifle_SemiAuto_Light_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Projectile_BattleRifle_SemiAuto_Light_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | BattleRifle_SemiAuto_Light_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 19 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 19 |
| Firearm critical/headshot multiplier | 1.8 |
| ARC armour multiplier | 0.4 |
| ARC armour propagation coefficient | 0.2 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 220 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 16 |
| Reload time stat, seconds | 2.14 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.0007 |
| Base partial-reload duration, seconds | 2.6 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 19 | 19 |
| Armor | 0.6 | 0.4 | 0.4 | 1 | 0.16 | 3.04 | 3.04 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 7.6 | 7.6 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 28.5 | 28.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 22.8 | 22.8 |

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
| Damage | 19 |
| Fire rate | 15.667 |
| Range | 51.763 |
| Stability | 75.578 |
| Agility | 66.498 |
| Stealth | 20 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/Curve_DamageFalloff_BattleRifle_SemiAuto_Light_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.66 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 4 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 30 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/DA_Item_BattleRifle_SemiAuto_Light_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Projectile_BattleRifle_SemiAuto_Light_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

No definition found in this snapshot.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Item_BattleRifle_SemiAuto_Light_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Projectile_BattleRifle_SemiAuto_Light_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_Projectile_BattleRifle_SemiAuto_Light_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/BP_WeaponQualitySet_BattleRifle_SemiAuto_Light_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/Curve_DamageFalloff_BattleRifle_SemiAuto_Light_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/Curve_DamageFalloff_BattleRifle_SemiAuto_Light_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/DA_Item_BattleRifle_SemiAuto_Light_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_SemiAuto_Light_01/DA_Item_BattleRifle_SemiAuto_Light_01.json)

</details>
