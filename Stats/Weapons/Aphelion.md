# Aphelion

[Weapons](README.md) · [Mechanics](Mechanics.md) · [ARC damage model](../ARC/Damage_Model.md)

**Ammo:** Energy · **Game ID:** `BattleRifle_EnergyBurst_01`

[Weapon blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Item_BattleRifle_EnergyBurst_01.json) · [Item config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/DA_Item_BattleRifle_EnergyBurst_01.json) · [Level modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_WeaponQualitySet_BattleRifle_EnergyBurst_01.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/BP_Projectile_BattleRifle_EnergyBurst_01.json) · [BP_Item_BattleRifle_Base](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/Shared/BaseClasses/BattleRifle_Base/BP_Item_BattleRifle_Base.json)

[Timing fields and game-code formulas](Mechanics.md#firing-and-reload-timers).

### Standard

| Stat | Value |
| --- | --- |
| Body damage / projectile | 25 |
| Headshot multiplier | 2× |
| ARC armor multiplier | 2.5× |
| ARC weak-point multiplier | 1× |
| Configured fire rate (RPM) | 700 |
| RPM interval (s) | 0.0857 |
| Magazine | 10 |
| Reload stat (s) | 3.5 |
| Cooldown (s) | 0.7 |
| Firing mode | Burst |
| Shots per burst | 2 |
| ARC armor propagation multiplier | 1× |
| Durability burn rate | 0.0009 |
| Partial-reload base duration (s) | 3.5 |

### Amplified

Default changes are relative to Standard; upgrade changes are relative to the Amplified default. Prerequisite changes are included where required.

| Upgrade | Stat changes | What it does | Game files |
| --- | --- | --- | --- |
| Default | Durability burn rate **−0.00045** | Amplified baseline. | [Amplified Durability](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_Ascended.json) · [Amplified blueprint](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Item_BattleRifle_EnergyBurst_01_Ascended.json) |
| Bigger Mag | Magazine **+6** | Increases the magazine capacity. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_BiggerMag.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_BiggerMag.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_BiggerMag.json) |
| Charged Burst | Body damage / projectile **−2.5**, Magazine **+2**, Max shots per burst **+2**, +60% vertical recoil, +60% horizontal recoil, Initial charge delay **+0.4 s (0 → 0.4 s)**, Charge time per extra shot **+0.4 s (0 → 0.4 s)** | Changes the firing mode to charge and release. The longer the charge is held, the more projectiles are fired upon release. Minimum charged burst (shots) **1**. Charge time per extra shot (s) **0.4**. Extra hipfire windup (s) **0.2**. Initial charge delay (s) **0.4**. Skip extra hipfire windup in combat. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_ChargedBurst.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_ChargedBurst.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst.json) |
| Incendiary Rounds | Burn **+0.5 thermal / 0.1 s tick**, **2 s** duration, **1** stack maximum | Adds an incendiary compound to the projectile, setting targets on fire when hit. 0.5 thermal damage every 0.1 s for 2 s, up to 1 stack. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncendiaryRounds.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_IncendiaryRounds.json) · [Projectile](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/BP_Projectile_BattleRifle_EnergyBurst_Incendiary.json) · [Burning effect](../Sources/PioneerGame/Content/Pioneer/Core/Gameplay/StatusEffects/GE_Burning_Small.json) |
| Increased Burst (requires Charged Burst) | Body damage / projectile **−2.5**, Magazine **+2**, Max shots per burst **+4**, +60% vertical recoil, +60% horizontal recoil, Initial charge delay **+0.4 s (0 → 0.4 s)**, Charge time per extra shot **+0.4 s (0 → 0.4 s)** | Increases the number of projectiles fired within a burst. Minimum charged burst (shots) **1**. Charge time per extra shot (s) **0.4**. Extra hipfire windup (s) **0.2**. Initial charge delay (s) **0.4**. Skip extra hipfire windup in combat. | [Upgrade](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/DA_Upgrade_BattleRifle_EnergyBurst_01_IncreasedBurst.json) · [Modifiers](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Upgrades/BP_UpgradeWeaponMod_BattleRifle_EnergyBurst_01_IncreasedBurst.json) · [Weapon config](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Ascended/Permutations/BP_Item_BattleRifle_EnergyBurst_01_ChargedBurst_IncreasedBurst.json) |

### Direct physical damage to ARC

Baseline damage per projectile at full exposure, before falloff and damage propagation. [ARC damage model](../ARC/Damage_Model.md)

| Part group | Damage |
| --- | --- |
| Normal | 25 |
| Armor | 25 |
| Sturdy | 10 |
| WeakPoint | 37.5 |
| Critical | 37.5 |
| Fragile | 30 |

### Damage falloff

| Distance (m) | Damage factor | Interpolation |
| --- | --- | --- |
| 0 | 1.001× | Linear |
| 15 | 1.001× | Linear |
| 150 | 1.001× | Linear |
| 170 | 0.6× | Linear |

[Game curve](../Sources/PioneerGame/Content/Pioneer/Items/Firearms/BattleRifle_EnergyBurst_01/Curve_DamageFalloff_BattleRifle_EnergyBurst_01.json)
