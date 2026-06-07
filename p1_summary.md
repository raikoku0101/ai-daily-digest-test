**1. Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution**
**著者**: Code2LoRA Authors et al. (2025)
**arXiv**: https://arxiv.org/abs/2606.06492

**まとめ**:
ハイパーネットワーク（hypernetwork）がリポジトリ全体を入力として受け取り、推論時のトークンオーバーヘッドなしにリポジトリ固有 LoRA アダプターを動的生成する手法 Code2LoRA を提案。静的スナップショット版（Code2LoRA-Static）と GRU による進化追跡版（Code2LoRA-Evo）の 2 バリアントを提供し、アサーション完成ベンチマーク RepoPeftBench で FFT+RAG 比 +9.9pp、リポジトリごとの LoRA 上界と同等の精度を達成。コード AI のリポジトリ理解を推論コスト増なしに実現する新アーキテクチャとして注目される。
