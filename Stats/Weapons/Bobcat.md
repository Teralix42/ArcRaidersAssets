[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Bobcat

Internal weapon id: `SMG_01`. Ammo: **LightAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 6 | 1 | 6 | 2 | 0.2 | 1 | 1,000 | 20 | 3.5 |
| II | 6 | 1 | 6 | 2 | 0.2 | 1 | 1,000 | 20 | 3 |
| III | 6 | 1 | 6 | 2 | 0.2 | 1 | 1,000 | 20 | 2.5 |
| IV | 6 | 1 | 6 | 2 | 0.2 | 1 | 1,000 | 20 | 2 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | SMG_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,000 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000671 |
| Base partial-reload duration, seconds | 2.18 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6 | 6 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.48 | 0.48 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.4 | 2.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9 | 9 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9 | 9 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.2 | 7.2 |

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
| Damage | 6 |
| Fire rate | 66.7 |
| Range | 43.95 |
| Stability | 31.9 |
| Agility | 73.1 |
| Stealth | 21 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_01/Curve_DamageFalloff_SMG_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.3 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json |
| Item | Content/Pioneer/Items/Firearms/SMG_01/DA_Item_SMG_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_01/BP_Projectile_SMG_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | SMG_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,000 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000604 |
| Base partial-reload duration, seconds | 2.18 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6 | 6 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.48 | 0.48 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.4 | 2.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9 | 9 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9 | 9 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.2 | 7.2 |

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
| Damage | 6 |
| Fire rate | 66.7 |
| Range | 43.95 |
| Stability | 33.9 |
| Agility | 73.1 |
| Stealth | 21 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_01/Curve_DamageFalloff_SMG_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.15 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json |
| Item | Content/Pioneer/Items/Firearms/SMG_01/DA_Item_SMG_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_01/BP_Projectile_SMG_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | SMG_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,000 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000537 |
| Base partial-reload duration, seconds | 2.18 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6 | 6 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.48 | 0.48 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.4 | 2.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9 | 9 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9 | 9 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.2 | 7.2 |

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
| Damage | 6 |
| Fire rate | 66.7 |
| Range | 43.95 |
| Stability | 35.9 |
| Agility | 73.1 |
| Stealth | 21 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_01/Curve_DamageFalloff_SMG_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json |
| Item | Content/Pioneer/Items/Firearms/SMG_01/DA_Item_SMG_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_01/BP_Projectile_SMG_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | SMG_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 6 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 6 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 0.2 |
| ARC armour propagation coefficient | 0.1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,000 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 20 |
| Reload time stat, seconds | 2 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00047 |
| Base partial-reload duration, seconds | 2.18 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 6 | 6 |
| Armor | 0.6 | 0.4 | 0.2 | 1 | 0.08 | 0.48 | 0.48 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.4 | 2.4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 9 | 9 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 9 | 9 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 7.2 | 7.2 |

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
| Damage | 6 |
| Fire rate | 66.7 |
| Range | 43.95 |
| Stability | 37.4 |
| Agility | 73.1 |
| Stealth | 21 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/SMG_01/Curve_DamageFalloff_SMG_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 13,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.85 |
| Multiply | 1 |

###### Firedispersionmax

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json |
| Item | Content/Pioneer/Items/Firearms/SMG_01/DA_Item_SMG_01.json |
| Quality set | Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/SMG_01/BP_Projectile_SMG_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

No definition found in this snapshot.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/BP_Item_SMG_01.json)
- [Content/Pioneer/Items/Firearms/SMG_01/BP_Projectile_SMG_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/BP_Projectile_SMG_01.json)
- [Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/BP_WeaponQualitySet_SMG_01.json)
- [Content/Pioneer/Items/Firearms/SMG_01/Curve_DamageFalloff_SMG_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/Curve_DamageFalloff_SMG_01.json)
- [Content/Pioneer/Items/Firearms/SMG_01/DA_Item_SMG_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/SMG_01/DA_Item_SMG_01.json)

</details>
