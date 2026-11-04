# Combat stats

### ARC machines

Frame and part HP, armor, weak points, and damage resistance for 26 machines. Part tables include resistance groups and health rules. [ARC stats](ARC/)

### Damage against Raiders

- **[Weapons](Weapons/README.md#damage-against-raiders)** — Body damage, headshot multipliers, fire rate, and magazine size. Each weapon page has upgrade stats, Amplified configs, falloff curves, and damage against ARC.
- **[Shields](Shields/)** — Shield strength, damage reduction, and run and sprint speed.

### Gadgets and consumables

| Item | Configured stats |
| --- | --- |
| Flame Spray | 1.3 fire damage per 0.1 s tick. Durability drains at 5% per second while firing. [Damage](Sources/PioneerGame/Content/Pioneer/Items/Gadgets/SprayCan_Fire/GE_SprayCan_Fire.json) · [Durability](Sources/PioneerGame/Content/Pioneer/Items/Gadgets/SprayCan_Fire/DA_Item_SprayCan_Fire.json) |
| Firefly Burner | Ignites on impact. The thrown burner has a 0.4 s ignition delay and a 3 s explosion timer. [Game config](Sources/PioneerGame/Content/Pioneer/Items/Throwable/FireflyPart_01/BP_WItem_Salvage_Hornetflamethrower_Part.json) |
| Adrenaline Shot | Usable at full stamina. Effect stacks are capped at one. [Item](Sources/PioneerGame/Content/Pioneer/Items/_GENERATED_/SimpleConsumable/AdrenalinShot/BP_Item_AdrenalinShot.json) · [Effect](Sources/PioneerGame/Content/Pioneer/Items/_GENERATED_/SimpleConsumable/AdrenalinShot/GE_AdrenalinShot.json) |

Extracted game configs and recovered damage rules. [Game files](Sources/)
