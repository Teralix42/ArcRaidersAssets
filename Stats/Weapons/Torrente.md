[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Torrente

Internal weapon id: `LMG_Medium_01`. Ammo: **MediumAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 8 | 1 | 8 | 2 | 1 | 1 | 800 | 60 | 8 |
| II | 8 | 1 | 8 | 2 | 1 | 1 | 800 | 70 | 7 |
| III | 8 | 1 | 8 | 2 | 1 | 1 | 800 | 80 | 6 |
| IV | 8 | 1 | 8 | 2 | 1 | 1 | 800 | 90 | 5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | LMG_Medium_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 800 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 60 |
| Reload time stat, seconds | 8 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000899 |
| Base partial-reload duration, seconds | 5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

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
| Damage | 8 |
| Fire rate | 58.33 |
| Range | 49.91 |
| Stability | 73.7 |
| Agility | 37.7 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/LMG_Medium_01/Curve_DamageFalloff_LMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | -10 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/LMG_Medium_01/DA_Item_LMG_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Projectile_LMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | LMG_Medium_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 800 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 70 |
| Reload time stat, seconds | 7 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000809 |
| Base partial-reload duration, seconds | 5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

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
| Damage | 8 |
| Fire rate | 58.33 |
| Range | 49.91 |
| Stability | 74.2 |
| Agility | 37.7 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/LMG_Medium_01/Curve_DamageFalloff_LMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Weapon | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/LMG_Medium_01/DA_Item_LMG_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Projectile_LMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | LMG_Medium_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 800 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 80 |
| Reload time stat, seconds | 6 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000719 |
| Base partial-reload duration, seconds | 5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

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
| Damage | 8 |
| Fire rate | 58.33 |
| Range | 49.91 |
| Stability | 74.2 |
| Agility | 37.7 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/LMG_Medium_01/Curve_DamageFalloff_LMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 10 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/LMG_Medium_01/DA_Item_LMG_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Projectile_LMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | LMG_Medium_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 8 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 8 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 800 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 90 |
| Reload time stat, seconds | 5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000629 |
| Base partial-reload duration, seconds | 5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 8 | 8 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.2 | 3.2 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 12 | 12 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 9.6 | 9.6 |

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
| Damage | 8 |
| Fire rate | 58.33 |
| Range | 49.91 |
| Stability | 74.7 |
| Agility | 37.7 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/LMG_Medium_01/Curve_DamageFalloff_LMG_Medium_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 1,500 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 15,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 17,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 20 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.7 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json |
| Item | Content/Pioneer/Items/Firearms/LMG_Medium_01/DA_Item_LMG_Medium_01.json |
| Quality set | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Projectile_LMG_Medium_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

No definition found in this snapshot.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Item_LMG_Medium_01.json)
- [Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Projectile_LMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_Projectile_LMG_Medium_01.json)
- [Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/BP_WeaponQualitySet_LMG_Medium_01.json)
- [Content/Pioneer/Items/Firearms/LMG_Medium_01/Curve_DamageFalloff_LMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/Curve_DamageFalloff_LMG_Medium_01.json)
- [Content/Pioneer/Items/Firearms/LMG_Medium_01/DA_Item_LMG_Medium_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/LMG_Medium_01/DA_Item_LMG_Medium_01.json)

</details>
