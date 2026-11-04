[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Dolabra

Internal weapon id: `Shotgun_Energy_Adjustable_01`. Ammo: **EnergyAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unlevelled | 25 | 19 | — | 1 | 1.5 | 1.5 | 55 | 8 | 3.25 |

#### Level Unlevelled

| Identity | Value |
| --- | --- |
| Id | Shotgun_Energy_Adjustable_01 |
| Level | — |
| Level label | Unlevelled |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 25 |
| Projectiles / simultaneous shot | 19 |
| Physical damage / full spread | — |
| Firearm critical/headshot multiplier | 1 |
| ARC armour multiplier | 1.5 |
| ARC armour propagation coefficient | 1.5 |
| ARC weakpoint multiplier | 1.5 |
| Fire rate stat, RPM | 55 |
| Firing mode | SemiAuto |
| Burst size stat | 1 |
| Magazine size | 8 |
| Reload time stat, seconds | 3.25 |
| Cooldown time stat, seconds | 0 |
| Durability burn rate stat | 0.003582 |
| Base partial-reload duration, seconds | 3.25 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 25 | — |
| Armor | 0.6 | 0.4 | 1.5 | 1 | 0.6 | 15 | — |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 10 | — |
| WeakPoint | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 56.25 | — |
| Critical | -0.5 | 1.5 | 1 | 1.5 | 2.25 | 56.25 | — |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 30 | — |

##### Upgrades

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Hits for full damage | 2 |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 50 |
| Fire rate | 8.7 |
| Range | 53.38 |
| Stability | 79.4 |
| Agility | 29.3 |
| Stealth | 1 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/Curve_DamageFalloff_Shotgun_Energy_Adjustable_01.json |

###### Keys

| Distance cm | Damage factor | Interpolation | Tangent mode | Tangent weight mode | Arrive tangent | Leave tangent | Arrive tangent weight | Leave tangent weight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 2,000 | 1.001 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |
| 10,000 | 0.8 | RCIM_Linear | RCTM_Auto | RCTWM_WeightedNone | 0 | 0 | 0 | 0 |

###### Stored settings not serialized

pre_infinity_extrapolation, post_infinity_extrapolation

##### Modifiers

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/BP_Item_Shotgun_Energy_Adjustable_01.json |
| Item | Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/DA_Item_Shotgun_Energy_Adjustable_01.json |
| Quality set | — |
| Quality function package | — |
| Projectile | Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/BP_Projectile_Shotgun_Energy_Adjustable_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/BP_Item_Shotgun_Energy_Adjustable_01.json

### Amplified configurations

No definition found in this snapshot.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/BP_Item_Shotgun_Energy_Adjustable_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/BP_Item_Shotgun_Energy_Adjustable_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/BP_Projectile_Shotgun_Energy_Adjustable_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/BP_Projectile_Shotgun_Energy_Adjustable_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/Curve_DamageFalloff_Shotgun_Energy_Adjustable_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/Curve_DamageFalloff_Shotgun_Energy_Adjustable_01.json)
- [Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/DA_Item_Shotgun_Energy_Adjustable_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shotgun_Energy_Adjustable_01/DA_Item_Shotgun_Energy_Adjustable_01.json)

</details>
