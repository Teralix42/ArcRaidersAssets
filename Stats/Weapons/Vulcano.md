[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Vulcano

Internal weapon id: `Shotgun_SemiAuto_01`. Ammo: **ShotgunAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I | 5.5 | 9 | 49.5 | 1 | 0.5 | 1 | 126 | 6 | 3.5 |
| II | 5.5 | 9 | 49.5 | 1 | 0.5 | 1 | 140 | 6 | 3 |
| III | 5.5 | 9 | 49.5 | 1 | 0.5 | 1 | 154 | 6 | 2.5 |
| IV | 5.5 | 9 | 49.5 | 1 | 0.5 | 1 | 168 | 6 | 2 |

#### Level I

| Identity | Value |
| --- | --- |
| Id | Shotgun_SemiAuto_01_Level1 |
| Level | 1 |
| Level label | I |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | 1 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 5.5 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 49.5 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 126 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.005563 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 5.5 | 49.5 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.1 | 9.9 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.2 | 19.8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 8.25 | 74.25 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 8.25 | 74.25 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 6.6 | 59.4 |

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
| Damage | 49.5 |
| Fire rate | 12.8 |
| Range | 22 |
| Stability | 66.1 |
| Agility | 65.3 |
| Stealth | 15 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/Curve_DamageFalloff_Shotgun_SemiAuto_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

###### Reloadtime

| Field | Value |
| --- | --- |
| Add | 0.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 0.9 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/DA_Item_Shotgun_SemiAuto_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Projectile_Shotgun_SemiAuto_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json, Script/PrecompiledScript.Cache

#### Level II

| Identity | Value |
| --- | --- |
| Id | Shotgun_SemiAuto_01_Level2 |
| Level | 2 |
| Level label | II |
| Variant | Standard |
| Quality index | 1 |
| Uses standard level | 2 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 5.5 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 49.5 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 140 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 3 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.005007 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 5.5 | 49.5 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.1 | 9.9 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.2 | 19.8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 8.25 | 74.25 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 8.25 | 74.25 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 6.6 | 59.4 |

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
| Damage | 49.5 |
| Fire rate | 14.3 |
| Range | 22 |
| Stability | 64.6 |
| Agility | 66.3 |
| Stealth | 15 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/Curve_DamageFalloff_Shotgun_SemiAuto_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/DA_Item_Shotgun_SemiAuto_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Projectile_Shotgun_SemiAuto_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json, Script/PrecompiledScript.Cache

#### Level III

| Identity | Value |
| --- | --- |
| Id | Shotgun_SemiAuto_01_Level3 |
| Level | 3 |
| Level label | III |
| Variant | Standard |
| Quality index | 2 |
| Uses standard level | 3 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 5.5 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 49.5 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 154 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2.5 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.00445 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 5.5 | 49.5 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.1 | 9.9 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.2 | 19.8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 8.25 | 74.25 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 8.25 | 74.25 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 6.6 | 59.4 |

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
| Damage | 49.5 |
| Fire rate | 15.8 |
| Range | 22 |
| Stability | 63.1 |
| Agility | 66.8 |
| Stealth | 15 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/Curve_DamageFalloff_Shotgun_SemiAuto_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/DA_Item_Shotgun_SemiAuto_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Projectile_Shotgun_SemiAuto_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json, Script/PrecompiledScript.Cache

#### Level IV

| Identity | Value |
| --- | --- |
| Id | Shotgun_SemiAuto_01_Level4 |
| Level | 4 |
| Level label | IV |
| Variant | Standard |
| Quality index | 3 |
| Uses standard level | 4 |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 5.5 |
| Projectiles / simultaneous shot | 9 |
| Physical damage / full spread | 49.5 |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 0.5 |
| ARC armour propagation coefficient | 0.4 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 168 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 6 |
| Reload time stat, seconds | 2 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.003894 |
| Base partial-reload duration, seconds | 2.8 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 5.5 | 49.5 |
| Armor | 0.6 | 0.4 | 0.5 | 1 | 0.2 | 1.1 | 9.9 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 2.2 | 19.8 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 8.25 | 74.25 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 8.25 | 74.25 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 6.6 | 59.4 |

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
| Damage | 49.5 |
| Fire rate | 17.3 |
| Range | 22 |
| Stability | 61.1 |
| Agility | 67.3 |
| Stealth | 15 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/Curve_DamageFalloff_Shotgun_SemiAuto_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 5,000 | 0.6 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

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

###### Firerate

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.2 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/DA_Item_Shotgun_SemiAuto_01.json |
| Quality set | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Projectile_Shotgun_SemiAuto_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json, Script/PrecompiledScript.Cache

### Amplified configurations

No definition found in this snapshot.

## Native default provenance

| Field | Value |
| --- | --- |
| Path | Script/PrecompiledScript.Cache |
| Sha256 | 120a31ba704fa8f9c634f8458d83f82fc2954fbe8b0a91d923a708584ebb59b8 |


<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Item_Shotgun_SemiAuto_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Projectile_Shotgun_SemiAuto_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_Projectile_Shotgun_SemiAuto_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/BP_WeaponQualitySet_Shotgun_SemiAuto_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/Curve_DamageFalloff_Shotgun_SemiAuto_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/Curve_DamageFalloff_Shotgun_SemiAuto_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/DA_Item_Shotgun_SemiAuto_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_SemiAuto_01/DA_Item_Shotgun_SemiAuto_01.json)

</details>
