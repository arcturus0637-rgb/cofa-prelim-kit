# v1.4 범용 최적화 선정 기록 (2026-11-02)

요청에 따라 버스 전용 `cofa-routing`, 고정 정류장 검사기와 그 전용 테스트를 현재 배포에서 제거했습니다. 일반 그래프·배정·흐름 방법은 다양한 문제에 쓰이므로 유지합니다. 새 원문은 수동 참고자료이고, 실제 문제의 모델·계산·검증·서비스는 Codex가 제공 프로젝트에 구현합니다. 특정 과제의 데이터·완성 답안·서비스를 미리 넣지 않았습니다.

## 추가한 공개 저장소

- [hajibabaie/combinatorial-optimization-skills](https://github.com/hajibabaie/combinatorial-optimization-skills): 76개 중 범용 12개 SKILL.md만 선정. LP, IP, 선형화, B&B, CP, DP, 네트워크 흐름, 배정, 검증, 기존 솔버 선택, 다목적, 코드 구조. MIT 원문/라이선스와 커밋을 보존했습니다. 확인 시점 GitHub 별15개로 채택 규모는 작으며, 인기나 예제 정확성을 품질 증명으로 보지 않습니다.
- [K-Dense-AI/scientific-agents의 optimization-scientist](https://github.com/K-Dense-AI/scientific-agents/tree/main/scientific-agents/optimization-scientist/skills/optimization-scientist): 연속·볼록/비볼록 모델·스케일링·수치해법 참고. MIT 원문과 LICENSE.md 보존. 확인 시점 별234개는 저장소 전체 수치이며 해당 스킬의 성능 측정이 아닙니다. 두 출처 모두 설치 횟수는 확인하지 못했습니다.

두 원본의 정확한 커밋/선택 경로는 sources.lock에 있습니다. 배차 전용 스킬은 선택하지 않았습니다. 원문의 의존성 설치·상용 솔버·추가 에이전트·강제 워크플로는 활성화하지 않습니다. [원문 선택 표와 수학적 보정](../skills/cofa-optimize/references/source-guide.md)을 먼저 읽고 필요한 문서만 참고합니다.

## 검토 후 제외

- [ShayanDarabi/operations-research-skill](https://github.com/ShayanDarabi/operations-research-skill): 폭넓지만 기존 선정 내용과 겹치고 압축 .skill 배포입니다. 내부 자료 검토에서 big-M 활성 분기 설명과 논리 함의 방향의 모순, 일반 비선형 KKT의 최적성 보장 과장, 설치/환경 가정을 발견해 포함하지 않았습니다.
- [K-Dense scientific-agent-skills의 pymoo](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/pymoo): 다목적 진화 최적화에 유용할 수 있지만 추가 의존성과 특화 실행환경이 필요합니다. Pareto 근사 결과를 전역 최적성으로 오해하지 않도록 이번 기본 묶음에서는 제외했습니다.
- NVIDIA cuOpt 계열: GPU/CUDA 등 제공 여부가 불명확한 실행 전제 때문에 제외. cvxgrp/cvx-sd-skill은 신호분해 특화로 범용 우선순위에서 제외했습니다.

## 실제 적용

`cofa-optimize`로 요구조건을 모델로 바꾸고 필요한 원문을 선택합니다. 제공된 솔버 또는 적합한 구조적 알고리즘으로 실제 입력의 해를 구하며 제약/목표를 독립 재계산합니다. `cofa-opt-service`로 이를 실제 API/화면·필수 저장/내보내기와 연결합니다. `cofa-explain`은 구현 파일·알고리즘·검증·최적성 근거/한계가 담긴 설명 산출물을 작성합니다.

시간 안에 풀기 어려운 문제까지 항상 전역 최적해를 찾는 스킬은 없습니다. exact 해법/증명을 먼저 검토하고, 한계가 있으면 가능해·최선해·유효 bound/gap·미충족 보장 범위를 솔직히 기록합니다. 제공 환경에 솔버가 없다면 설치하지 않고 구조적/표준 라이브러리 대안을 검토합니다.
