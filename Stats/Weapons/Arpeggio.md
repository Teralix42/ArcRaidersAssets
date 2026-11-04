[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Arpeggio

Internal weapon id: `AssaultRifle_Burst_01`. Ammo: **MediumAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 9.5 | 1 | 9.5 | 2 | 1 | 1 | 1,100 | 24 | 4 |
| II | 9.5 | 1 | 9.5 | 2 | 1 | 1 | 1,100 | 24 | 3.5 |
| III | 9.5 | 1 | 9.5 | 2 | 1 | 1 | 1,100 | 24 | 3 |
| IV | 9.5 | 1 | 9.5 | 2 | 1 | 1 | 1,100 | 24 | 2.5 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Burst_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,100 |
| Firing mode | burst |
| Burst size stat | 3 |
| Magazine size | 24 |
| Reload time stat, seconds | 4 |
| Cooldown time stat, seconds | 0.5 |
| Durability burn rate stat | 0.001378 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9.5 | 9.5 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.8 | 3.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.8 | 3.8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 14.25 | 14.25 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 14.25 | 14.25 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 11.4 | 11.4 |

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
| Damage | 9.5 |
| Fire rate | 7.33 |
| Range | 55.91 |
| Stability | 79.5 |
| Agility | 57.3 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/Curve_DamageFalloff_AssaultRifle_Burst_01.json |

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

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | 0.1 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 1 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/DA_Item_AssaultRifle_Burst_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Projectile_AssaultRifle_Burst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Burst_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,100 |
| Firing mode | burst |
| Burst size stat | 3 |
| Magazine size | 24 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.4 |
| Durability burn rate stat | 0.00124 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9.5 | 9.5 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.8 | 3.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.8 | 3.8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 14.25 | 14.25 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 14.25 | 14.25 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 11.4 | 11.4 |

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
| Damage | 9.5 |
| Fire rate | 13.33 |
| Range | 55.91 |
| Stability | 78 |
| Agility | 57.3 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/Curve_DamageFalloff_AssaultRifle_Burst_01.json |

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
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burnrate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/DA_Item_AssaultRifle_Burst_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Projectile_AssaultRifle_Burst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Burst_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,100 |
| Firing mode | burst |
| Burst size stat | 3 |
| Magazine size | 24 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0.3 |
| Durability burn rate stat | 0.001102 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9.5 | 9.5 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.8 | 3.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.8 | 3.8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 14.25 | 14.25 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 14.25 | 14.25 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 11.4 | 11.4 |

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
| Damage | 9.5 |
| Fire rate | 21.83 |
| Range | 55.91 |
| Stability | 75.5 |
| Agility | 57.3 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/Curve_DamageFalloff_AssaultRifle_Burst_01.json |

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

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.1 |
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
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/DA_Item_AssaultRifle_Burst_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Projectile_AssaultRifle_Burst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Burst_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 9.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 9.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 1 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 1,100 |
| Firing mode | burst |
| Burst size stat | 3 |
| Magazine size | 24 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0.2 |
| Durability burn rate stat | 0.000965 |
| Base partial-reload duration, seconds | 2.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 9.5 | 9.5 |
| Armor | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.8 | 3.8 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 3.8 | 3.8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 14.25 | 14.25 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 14.25 | 14.25 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 11.4 | 11.4 |

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
| Damage | 9.5 |
| Fire rate | 36.33 |
| Range | 55.91 |
| Stability | 72 |
| Agility | 57.3 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/Curve_DamageFalloff_AssaultRifle_Burst_01.json |

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

###### Cooldowntime

| Field | Value |
| --- | --- |
| Add | -0.2 |
| Addmultiply | 1 |
| Multiply | 1 |

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
| Addmultiply | 0.7 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/DA_Item_AssaultRifle_Burst_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Projectile_AssaultRifle_Burst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json, Script/PrecompiledScript.Cache

### Amplified configurations

No definition found in this snapshot.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Item_AssaultRifle_Burst_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Projectile_AssaultRifle_Burst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_Projectile_AssaultRifle_Burst_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/BP_WeaponQualitySet_AssaultRifle_Burst_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/Curve_DamageFalloff_AssaultRifle_Burst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/Curve_DamageFalloff_AssaultRifle_Burst_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/DA_Item_AssaultRifle_Burst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Burst_01/DA_Item_AssaultRifle_Burst_01.json)
- [Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/AssaultRifle_Base/BP_Item_AssaultRifle_Base.json)

</details>
