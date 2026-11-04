# ARC stats

[Combat stats](../README.md) · [Stat renders](Renders/) · [Stats models](Models/) · [Damage model](Damage_Model.md) · [JSON](arc_parts.json)

Health, armor and weak points for 26 ARC machines. Frame HP comes from the machine's frame rule. Thrusters, armor plates and other parts can have their own HP and pass damage along to the frame.

A Wasp has **30 HP per thruster**. Each thruster is marked Fragile and takes **1.2×** base physical damage. Armor starts at **0.4×**, with a separate modifier for each weapon. [Wasp](Wasp.md) · [Damage model](Damage_Model.md)

| ARC | Frame HP | Stats model |
| --- | --- | --- |
| [ARC Reclaimer](Reclaimer.md) | 830 | [Blend](Models/Reclaimer.blend) |
| [ARC Surveyor](Surveyor.md) | 257 | [Blend](Models/Surveyor.blend) |
| [ARC Turbine](Turbine.md) | 4000 | [Blend](Models/Turbine.blend) |
| [Bastion](Bastion.md) | 2050 | [Blend](Models/Bastion.blend) |
| [Bombardier](Bombardier.md) | 2670 | [Blend](Models/Bombardier.blend) |
| [Bully](Bully.md) | 3000 | [Blend](Models/Bully.blend) |
| [Comet](Comet.md) | 150 | [Blend](Models/Comet.blend) |
| [Fireball](Fireball.md) | 20 | [Blend](Models/Fireball.blend) |
| [Firefly](Firefly.md) | 200 | [Blend](Models/Firefly.blend) |
| [Frigate Cannon](Frigate%20Cannon.md) | 999999 | — |
| [Hornet](Hornet.md) | 200 | [Blend](Models/Hornet.blend) |
| [Hydra](Hydra.md) | 1050 | [Blend](Models/Hydra.blend) |
| [Leaper](Leaper.md) | 1100 | [Blend](Models/Leaper.blend) |
| [Matriarch](Matriarch.md) | 23100 | [Blend](Models/Matriarch.blend) |
| [Pop](Pop.md) | 20 | [Blend](Models/Pop.blend) |
| [Queen](Queen.md) | 23100 | [Blend](Models/Queen.blend) |
| [Rocketeer](Rocketeer.md) | 1100 | [Blend](Models/Rocketeer.blend) |
| [Sentinel](Sentinel.md) | 300 | [Blend](Models/Sentinel.blend) |
| [Shredder](Shredder.md) | 385 | [Blend](Models/Shredder.blend) |
| [Skulker](Skulker.md) | 230 | [Blend](Models/Skulker.blend) |
| [Snitch](Snitch.md) | 158 | [Blend](Models/Snitch.blend) |
| [Spotter](Spotter.md) | 80 | [Blend](Models/Spotter.blend) |
| [Tick](Tick.md) | 10 | [Blend](Models/Tick.blend) |
| [Turret](Turret.md) | 80 | [Blend](Models/Turret.blend) |
| [Vaporizer](Vaporizer.md) | 1500 | [Blend](Models/Vaporizer.blend) |
| [Wasp](Wasp.md) | 110 | [Blend](Models/Wasp.blend) |

### Renders and Blender models

Open a machine for its part health, break-off, scavenging and damage target views. Layer A shows the innermost structure. The last layer shows the full machine. Start with the **Part Health** view to see the HP colors, then use the table for exact values. [Rocketeer layers](Rocketeer.md#layers-and-views)

The Blender files have packed textures. Run `RUN ARC Inspector.py` to use the ARC Inspector sidebar and click through the parts and layers.
