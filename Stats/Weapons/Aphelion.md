[Weapon index](README.md) · [Definitions and mechanics](Mechanics.md) · [JSON data](weapons.json)

# Aphelion

Internal weapon id: `BattleRifle_EnergyBurst_01`. Ammo: **EnergyAmmo**.

### Standard levels

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unlevelled | 25 | 1 | 25 | 2 | 2.5 | 1 | 700 | 10 | 3.5 |

#### Level Unlevelled

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01 |
| Level | — |
| Level label | Unlevelled |
| Variant | Standard |
| Quality index | 0 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 25 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 25 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 2 |
| Magazine size | 10 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.0009 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 25 | 25 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 25 | 25 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 10 | 10 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 30 | 30 |

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
| Damage | 25 |
| Fire rate | 10.182 |
| Range | 75.597 |
| Stability | 76.449 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Item_BattleRifle_EnergyBurst_01.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/DA_Item_BattleRifle_EnergyBurst_01.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Item_BattleRifle_EnergyBurst_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json, Script/PrecompiledScript.Cache

### Amplified configurations

| Level / variant | Damage / projectile | Projectiles | Full spread | Crit × | ARC armour × | ARC weakpoint × | RPM | Magazine | Reload stat, s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | 25 | 1 | 25 | 2 | 2.5 | 1 | 700 | 10 | 3.5 |
| Bigger Mag | 25 | 1 | 25 | 2 | 2.5 | 1 | 700 | 16 | 3.5 |
| Bigger Mag + Charged Burst | 22.5 | 1 | 22.5 | 2 | 2.5 | 1 | 700 | 18 | 3.5 |
| Bigger Mag + Charged Burst + Incendiary Rounds | 22.5 | 1 | 22.5 | 2 | 2.5 | 1 | 700 | 18 | 3.5 |
| Bigger Mag + Charged Burst + Increased Burst | 22.5 | 1 | 22.5 | 2 | 2.5 | 1 | 700 | 18 | 3.5 |
| Bigger Mag + Charged Burst + Increased Burst + Incendiary Rounds | 22.5 | 1 | 22.5 | 2 | 2.5 | 1 | 700 | 18 | 3.5 |
| Bigger Mag + Incendiary Rounds | 25 | 1 | 25 | 2 | 2.5 | 1 | 700 | 16 | 3.5 |
| Charged Burst | 22.5 | 1 | 22.5 | 2 | 2.5 | 1 | 700 | 12 | 3.5 |
| Charged Burst + Incendiary Rounds | 22.5 | 1 | 22.5 | 2 | 2.5 | 1 | 700 | 12 | 3.5 |
| Charged Burst + Increased Burst | 22.5 | 1 | 22.5 | 2 | 2.5 | 1 | 700 | 12 | 3.5 |
| Charged Burst + Increased Burst + Incendiary Rounds | 22.5 | 1 | 22.5 | 2 | 2.5 | 1 | 700 | 12 | 3.5 |
| Incendiary Rounds | 25 | 1 | 25 | 2 | 2.5 | 1 | 700 | 10 | 3.5 |

#### Amplified — Default

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Level | 5 |
| Level label | Amplified |
| Variant | Default |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 25 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 25 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 2 |
| Magazine size | 10 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 25 | 25 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 25 | 25 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 10 | 10 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 30 | 30 |

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
| Damage | 25 |
| Fire rate | 10.182 |
| Range | 75.597 |
| Stability | 76.449 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Item_BattleRifle_EnergyBurst_01_Ascended.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/DA_Item_BattleRifle_EnergyBurst_01_Ascended.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Item_BattleRifle_EnergyBurst_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 25 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 25 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 2 |
| Magazine size | 16 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 25 | 25 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 25 | 25 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 10 | 10 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 30 | 30 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 6 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

None.

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 25 |
| Fire rate | 10.182 |
| Range | 75.597 |
| Stability | 76.449 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 6 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Item_BattleRifle_EnergyBurst_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag + Charged Burst

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag + Charged Burst |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 22.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 22.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 4 |
| Magazine size | 18 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 22.5 | 22.5 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 22.5 | 22.5 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9 | 9 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 27 | 27 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 6 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Charged Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst |
| Name | Charged Burst |
| Description | Changes the firing mode to charge and release. The longer the charge is held, the more projectiles are fired upon release. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Minimum burst size | 1 |
| Charge time per extra shot s | 0.4 |
| Extra hipfire windup s | 0.2 |
| First charge delay s | 0.4 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 22.5 |
| Fire rate | 16.716 |
| Range | 75.597 |
| Stability | 71.911 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 8 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag + Charged Burst + Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag + Charged Burst + Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 22.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 22.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 4 |
| Magazine size | 18 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 22.5 | 22.5 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 22.5 | 22.5 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9 | 9 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 27 | 27 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 6 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Charged Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst |
| Name | Charged Burst |
| Description | Changes the firing mode to charge and release. The longer the charge is held, the more projectiles are fired upon release. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Minimum burst size | 1 |
| Charge time per extra shot s | 0.4 |
| Extra hipfire windup s | 0.2 |
| First charge delay s | 0.4 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 22.5 |
| Fire rate | 16.716 |
| Range | 75.597 |
| Stability | 71.911 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 8 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Projectile_BattleRifle_EnergyBurst_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag + Charged Burst + Increased Burst

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag + Charged Burst + Increased Burst |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 22.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 22.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 6 |
| Magazine size | 18 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 22.5 | 22.5 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 22.5 | 22.5 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9 | 9 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 27 | 27 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 6 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Charged Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst |
| Name | Charged Burst |
| Description | Changes the firing mode to charge and release. The longer the charge is held, the more projectiles are fired upon release. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Increased Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncreasedBurst |
| Name | Increased Burst |
| Description | Increases the number of projectiles fired within a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncreasedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Minimum burst size | 1 |
| Charge time per extra shot s | 0.4 |
| Extra hipfire windup s | 0.2 |
| First charge delay s | 0.4 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 22.5 |
| Fire rate | 21.266 |
| Range | 75.597 |
| Stability | 70.717 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 8 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Burstsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag + Charged Burst + Increased Burst + Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag + Charged Burst + Increased Burst + Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 22.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 22.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 6 |
| Magazine size | 18 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 22.5 | 22.5 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 22.5 | 22.5 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9 | 9 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 27 | 27 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 6 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Charged Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst |
| Name | Charged Burst |
| Description | Changes the firing mode to charge and release. The longer the charge is held, the more projectiles are fired upon release. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Increased Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncreasedBurst |
| Name | Increased Burst |
| Description | Increases the number of projectiles fired within a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncreasedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Minimum burst size | 1 |
| Charge time per extra shot s | 0.4 |
| Extra hipfire windup s | 0.2 |
| First charge delay s | 0.4 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 22.5 |
| Fire rate | 21.266 |
| Range | 75.597 |
| Stability | 70.717 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 8 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Burstsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Projectile_BattleRifle_EnergyBurst_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Bigger Mag + Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Bigger Mag + Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 25 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 25 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 2 |
| Magazine size | 16 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 25 | 25 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 25 | 25 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 10 | 10 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 30 | 30 |

##### Upgrades

###### Bigger Mag

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_BiggerMag |
| Name | Bigger Mag |
| Description | Increases the magazine capacity. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 6 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

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
| Damage | 25 |
| Fire rate | 10.182 |
| Range | 75.597 |
| Stability | 76.449 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 6 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Projectile_BattleRifle_EnergyBurst_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Item_BattleRifle_EnergyBurst_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Charged Burst

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst |
| Level | 5 |
| Level label | Amplified |
| Variant | Charged Burst |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 22.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 22.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 4 |
| Magazine size | 12 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 22.5 | 22.5 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 22.5 | 22.5 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9 | 9 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 27 | 27 |

##### Upgrades

###### Charged Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst |
| Name | Charged Burst |
| Description | Changes the firing mode to charge and release. The longer the charge is held, the more projectiles are fired upon release. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Minimum burst size | 1 |
| Charge time per extra shot s | 0.4 |
| Extra hipfire windup s | 0.2 |
| First charge delay s | 0.4 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 22.5 |
| Fire rate | 16.716 |
| Range | 75.597 |
| Stability | 71.911 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Charged Burst + Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Charged Burst + Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 22.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 22.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 4 |
| Magazine size | 12 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 22.5 | 22.5 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 22.5 | 22.5 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9 | 9 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 27 | 27 |

##### Upgrades

###### Charged Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst |
| Name | Charged Burst |
| Description | Changes the firing mode to charge and release. The longer the charge is held, the more projectiles are fired upon release. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Minimum burst size | 1 |
| Charge time per extra shot s | 0.4 |
| Extra hipfire windup s | 0.2 |
| First charge delay s | 0.4 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 22.5 |
| Fire rate | 16.716 |
| Range | 75.597 |
| Stability | 71.911 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Projectile_BattleRifle_EnergyBurst_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Charged Burst + Increased Burst

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst |
| Level | 5 |
| Level label | Amplified |
| Variant | Charged Burst + Increased Burst |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 22.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 22.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 6 |
| Magazine size | 12 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 22.5 | 22.5 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 22.5 | 22.5 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9 | 9 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 27 | 27 |

##### Upgrades

###### Charged Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst |
| Name | Charged Burst |
| Description | Changes the firing mode to charge and release. The longer the charge is held, the more projectiles are fired upon release. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Increased Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncreasedBurst |
| Name | Increased Burst |
| Description | Increases the number of projectiles fired within a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncreasedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Minimum burst size | 1 |
| Charge time per extra shot s | 0.4 |
| Extra hipfire windup s | 0.2 |
| First charge delay s | 0.4 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 22.5 |
| Fire rate | 21.266 |
| Range | 75.597 |
| Stability | 70.717 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burstsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Charged Burst + Increased Burst + Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Charged Burst + Increased Burst + Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 22.5 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 22.5 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 6 |
| Magazine size | 12 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 22.5 | 22.5 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 22.5 | 22.5 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 9 | 9 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 33.75 | 33.75 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 27 | 27 |

##### Upgrades

###### Charged Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_ChargedBurst |
| Name | Charged Burst |
| Description | Changes the firing mode to charge and release. The longer the charge is held, the more projectiles are fired upon release. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Physicaldamage**

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

**Verticalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Horizontalrecoil**

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

**Clipsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Increased Burst

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncreasedBurst |
| Name | Increased Burst |
| Description | Increases the number of projectiles fired within a burst. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncreasedBurst.json |
| Modifier source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.json |
| Modifier function source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.uasset |
| Modifier selection | decoded_ModifyWeaponAttributes |

**Modifiers**

**Burstsize**

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

##### Extra damage effects

None.

##### Secondary effects

None.

##### Conditional mechanics

| Field | Value |
| --- | --- |
| Minimum burst size | 1 |
| Charge time per extra shot s | 0.4 |
| Extra hipfire windup s | 0.2 |
| First charge delay s | 0.4 |
| Skip extra windup in combat | Yes |

##### Ui stat scores

| Field | Value |
| --- | --- |
| Damage | 22.5 |
| Fire rate | 21.266 |
| Range | 75.597 |
| Stability | 70.717 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

###### Physicaldamage

| Field | Value |
| --- | --- |
| Add | -2.5 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Verticalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Horizontalrecoil

| Field | Value |
| --- | --- |
| Add | 0 |
| Addmultiply | 1.6 |
| Multiply | 1 |

###### Clipsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

###### Burstsize

| Field | Value |
| --- | --- |
| Add | 2 |
| Addmultiply | 1 |
| Multiply | 1 |

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Projectile_BattleRifle_EnergyBurst_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

#### Amplified — Incendiary Rounds

| Identity | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncendiaryRounds |
| Level | 5 |
| Level label | Amplified |
| Variant | Incendiary Rounds |
| Quality index | 3 |
| Uses standard level | — |

| Stat | Value |
| --- | --- |
| Physical damage / projectile | 25 |
| Projectiles / simultaneous shot | 1 |
| Physical damage / full spread | 25 |
| Firearm critical/headshot multiplier | 2 |
| ARC armour multiplier | 2.5 |
| ARC armour propagation coefficient | 1 |
| ARC weakpoint multiplier | 1 |
| Fire rate stat, RPM | 700 |
| Firing mode | burst |
| Burst size stat | 2 |
| Magazine size | 10 |
| Reload time stat, seconds | 3.5 |
| Cooldown time stat, seconds | 0.7 |
| Durability burn rate stat | 0.00045 |
| Base partial-reload duration, seconds | 3.5 |
| Uses shell/looping reload | No |
| Base shell-reload entry, seconds | — |
| Base shell-reload loop, seconds | — |
| Base shell-reload exit, seconds | — |
| Shells loaded per loop | — |

##### Direct physical ARC damage by part resistance

Normalized direct physical damage to one part at distance multiplier 1 and exposure 1, before health propagation. Special charge/ramp mechanics and other attack modifiers remain separate.

| Part group | Part R | Baseline × | Applied armour × | Applied weakpoint × | Effective × | Damage / projectile | Full-spread damage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | 0 | 1 | 1 | 1 | 1 | 25 | 25 |
| Armor | 0.6 | 0.4 | 2.5 | 1 | 1 | 25 | 25 |
| Sturdy | 0.6 | 0.4 | 1 | 1 | 0.4 | 10 | 10 |
| WeakPoint | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Critical | -0.5 | 1.5 | 1 | 1 | 1.5 | 37.5 | 37.5 |
| Fragile | -0.2 | 1.2 | 1 | 1 | 1.2 | 30 | 30 |

##### Upgrades

###### Incendiary Rounds

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_IncendiaryRounds |
| Name | Incendiary Rounds |
| Description | Adds an incendiary compound to the projectile, setting targets on fire when hit. |
| Is amplification root | No |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncendiaryRounds.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

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
| Damage | 25 |
| Fire rate | 10.182 |
| Range | 75.597 |
| Stability | 76.449 |
| Agility | 46.689 |
| Stealth | 16 |

##### Damage falloff

| Field | Value |
| --- | --- |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json |

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

None.

##### Source paths

| Field | Value |
| --- | --- |
| Weapon | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_IncendiaryRounds.json |
| Item | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_IncendiaryRounds.json |
| Quality set | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json |
| Quality function package | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.uasset |
| Projectile | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Projectile_BattleRifle_EnergyBurst_Incendiary.json |

###### Inherited stat sources

Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Item_BattleRifle_EnergyBurst_01.json, Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json, Script/PrecompiledScript.Cache

##### Amplification

| Field | Value |
| --- | --- |
| Durability burn rate base scale | 0.5 |

###### Base upgrade definitions

**Amplified Durability**

| Field | Value |
| --- | --- |
| Id | BattleRifle_EnergyBurst_01_Ascended |
| Name | Amplified Durability |
| Description | Amplified weapons have a higher maximum durability. |
| Is amplification root | Yes |
| Source path | Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json |
| Modifier source path | — |
| Modifier function source path | — |
| Modifier selection | no_WeaponMod_reference |

**Modifiers**

None.

<details>
<summary>Actual game source files</summary>

- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Item_BattleRifle_EnergyBurst_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Item_BattleRifle_EnergyBurst_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Projectile_BattleRifle_EnergyBurst_Incendiary.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Projectile_BattleRifle_EnergyBurst_Incendiary.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/DA_Item_BattleRifle_EnergyBurst_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/DA_Item_BattleRifle_EnergyBurst_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_ChargedBurst_IncreasedBurst_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_BiggerMag_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/DA_Item_BattleRifle_EnergyBurst_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/UniqueWeapons/BP_Item_BattleRifle_EnergyBurst_ChargedBurst_Base.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_BiggerMag.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_BiggerMag.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncendiaryRounds.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncendiaryRounds.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncreasedBurst.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncreasedBurst.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Item_BattleRifle_EnergyBurst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Item_BattleRifle_EnergyBurst_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json)
- [Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/DA_Item_BattleRifle_EnergyBurst_01.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/DA_Item_BattleRifle_EnergyBurst_01.json)
- [Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json)

</details>
