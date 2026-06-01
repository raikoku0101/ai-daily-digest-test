**3. DEMON: Diffusion Engine for Musical Orchestrated Noise**
**著者**: DEMON Team et al. (2025)
**arXiv**: https://arxiv.org/abs/2605.28657

**まとめ**:
音声生成拡散モデルをライブ演奏可能なリアルタイム楽器として実装するシステム。StreamDiffusionのリングバッファにPer-slot独立タイムステップスケジューリングやSDE source blendingを組み合わせ、RTX 5090で60秒楽曲を毎秒12.3回生成可能。フレーム単位でパラメータ制御でき、従来のチャンク単位制御の自己回帰型システムと異なる演奏体験を実現。消費者向けGPUで動作し、DAWやシンセサイザーに近い感覚でAI音楽生成を「演奏」できる新しいインターフェースを開拓した。
