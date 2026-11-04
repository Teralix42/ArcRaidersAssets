[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Tempest

Internal weapon id: `AssaultRifle_Bullpup_01`. Ammo: **MediumAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 10 | 1 | 10 | 1.5 | 0.8 | 1 | 550 | 25 | 3.75 |
| II | 10 | 1 | 10 | 1.5 | 0.8 | 1 | 550 | 25 | 3.25 |
| III | 10 | 1 | 10 | 1.5 | 0.8 | 1 | 550 | 25 | 2.75 |
| IV | 10 | 1 | 10 | 1.5 | 0.8 | 1 | 550 | 25 | 2.25 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Bullpup_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 550 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 25 |
| Reload time stat, seconds | 3.75 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.001056 |
| Base partial-reload duration, seconds | 2.57333 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

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
| Damage | 10 |
| Fire rate | 36.67 |
| Range | 55.94 |
| Stability | 67.4 |
| Agility | 50 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/Curve_DamageFalloff_AssaultRifle_Bullpup_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/DA_Item_AssaultRifle_Bullpup_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Projectile_AssaultRifle_Bullpup_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Bullpup_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 550 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 25 |
| Reload time stat, seconds | 3.25 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00095 |
| Base partial-reload duration, seconds | 2.57333 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

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
| Damage | 10 |
| Fire rate | 36.67 |
| Range | 55.94 |
| Stability | 67.9 |
| Agility | 50 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/Curve_DamageFalloff_AssaultRifle_Bullpup_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/DA_Item_AssaultRifle_Bullpup_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Projectile_AssaultRifle_Bullpup_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Bullpup_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 550 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 25 |
| Reload time stat, seconds | 2.75 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000845 |
| Base partial-reload duration, seconds | 2.57333 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

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
| Damage | 10 |
| Fire rate | 36.67 |
| Range | 55.94 |
| Stability | 68.4 |
| Agility | 50 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/Curve_DamageFalloff_AssaultRifle_Bullpup_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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
| Addmultiply | 0.8 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.8 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/DA_Item_AssaultRifle_Bullpup_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Projectile_AssaultRifle_Bullpup_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | AssaultRifle_Bullpup_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 10 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 10 |
| Firearm critical/headshot multiplier | 1.5 |
| ARC armour multiplier | 0.8 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 550 |
| Firing mode | Auto |
| Burst size stat | 1 |
| Magazine size | 25 |
| Reload time stat, seconds | 2.25 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.000739 |
| Base partial-reload duration, seconds | 2.57333 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 10 | 10 |
| Armor | 0.6 | 0.4 | 0.8 | 1 | 0.32 | 3.2 | 3.2 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 4 | 4 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 15 | 15 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 12 | 12 |

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
| Damage | 10 |
| Fire rate | 36.67 |
| Range | 55.94 |
| Stability | 68.4 |
| Agility | 50 |
| Stealth | 14 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/Curve_DamageFalloff_AssaultRifle_Bullpup_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 500 | 1.2 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
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
| Addmultiply | 0.7 |
| Multiply | 1 |

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | -0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.6 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json |
| Item | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/DA_Item_AssaultRifle_Bullpup_01.json |
| Quality set | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Projectile_AssaultRifle_Bullpup_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

No definition found in this snapshot.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Item_AssaultRifle_Bullpup_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Projectile_AssaultRifle_Bullpup_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_Projectile_AssaultRifle_Bullpup_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/BP_WeaponQualitySet_AssaultRifle_Bullpup_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/Curve_DamageFalloff_AssaultRifle_Bullpup_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/Curve_DamageFalloff_AssaultRifle_Bullpup_01.json)
- [Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/DA_Item_AssaultRifle_Bullpup_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/AssaultRifle_Bullpup_01/DA_Item_AssaultRifle_Bullpup_01.json)

</details>
