# 원본과 선택 범위

정확한커밋/경로는`config/sources.lock.json`,각배포파일의SHA-256은`bundle-lock.json`에있습니다. 원본파일내용은변경하지않았고선택한경로만보관했습니다. `skills/cofa-*`는이키트에서새로작성한대회용연결지침입니다. 원본전체워크플로를모두활성화하지않습니다.

| 원본 | 보관범위 | 적용방식 |
|---|---|---|
| https://github.com/obra/superpowers | systematic-debugging, verification-before-completion와해당지원파일 | 원인조사·검증지침을필요할때참조 |
| https://github.com/anthropics/claude-plugins-official | code-simplifier에이전트원문과라이선스 | Codex용cofa-simplify에서원문참조;Claude실행안함 |
| https://github.com/mattpocock/skills | engineering전체와handoff | 기본은diagnosing-bugs/code-review/tdd등필요한것만참조;외부이슈/PR/설정자동실행안함 |
| https://github.com/supabase/agent-skills | supabase, supabase-postgres-best-practices | SQL/실제제공Supabase환경에한해참조;클라우드계정생성안함 |
| https://github.com/multica-ai/andrej-karpathy-skills | karpathy-guidelines | Karpathy발언에서영감을받은제3자지침;Karpathy본인제작/공식배포로표시안함 |
| https://github.com/DietrichGebert/ponytail | ponytail, review, audit, debt | 최소완전변경·행동보존단순화;hook/프록시설치안함 |
| https://github.com/JuliusBrussee/caveman | 기본voice/review, investigate-first, lean-build, surgical-patch, safe-refactor, verify-and-stop | 간결한설명/국소수정참고;CLI·라우팅·브라우징·클라우드·텔레메트리제외 |

원본에있는설치명령/전역설정/외부API/다른모델/브라우저자동화지시는수행지시가아닌참고자료입니다. 실제과제/플랫폼/호스트권한과대회용어댑터의범위를먼저확인합니다. 원본의유용한기술적방법만선택합니다.

각원본LICENSE/NOTICE와하위라이선스를보존했습니다. Karpathy-inspired원본은SKILL프런트매터에MIT를선언하지만해당커밋에루트LICENSE본문은없어이사실을`LICENSE-DECLARATION.txt`에기록했습니다. 나머지원본의MIT/Apache등조건은각스냅샷원문을확인하세요. 새코드는루트LICENSE를따르고제3자원본의조건을대체하지않습니다.

`config/libraries.lock.json`의ReactFlow,DuckDB,MarkItDown,Vitest,Ruff,NetworkX,OR-Tools는사용자가선택한라이브러리입니다. 개인 PC에서 확인한 참고 버전과 원본 주소를 보관했으며 전체 실행 코드를 복사하지는 않았습니다. v1.1은 Git Clone 전용이며 추가 패키지 설치를 하지 않습니다. 제공 환경의 기존 도구를 사용합니다.

추가디버깅/단순화프로젝트는불필요하다고판단했습니다. 이미Superpowers+Matt의진단,code-simplifier+Ponytail+Karpathy의단순화,Caveman의국소수정참고가겹칩니다. 원본의벤치마크수치/토큰절약주장은이키트나대회환경에서재현했다고표시하지않습니다.


## v1.2 추가 원본과 적용 범위

- **Trail of Bits**: https://github.com/trailofbits/skills . Property-Based Testing의 SKILL과 참고 문서 5개, 원본 LICENSE를 보관합니다. 원본은 CC BY-SA 4.0입니다. `cofa-test-design`은 이를 대회용으로 각색한 어댑터이며 같은 라이선스, 출처와 변경 사실을 명시합니다. 원본의 프레임워크 추가 제안은 실행하지 않습니다. 기존 런타임/표준 라이브러리 검사로 대체할 수 있습니다.
- **Vercel**: https://github.com/vercel-labs/agent-skills . React Best Practices의 SKILL, AGENTS, metadata와 rules를 보관합니다. SKILL은 MIT를 선언하지만 고정 커밋에는 LICENSE/NOTICE/COPYING 파일이 없습니다. 이 사실을 LICENSE-DECLARATION.txt에 기록했고 원문/헤더를 유지했습니다. 실제 React/Next.js 과제에서 필요한 지침만 읽습니다. 배포 도구, MCP, 계정, 설치 스크립트는 포함하지 않습니다.

출처별 정확한 커밋과 선택 파일은 sources.lock에 있습니다. 새 원본의 기술 문서를 수동 참고할 뿐 자체 SKILL/agents 설정을 발견 경로에 등록하지 않습니다. Inquisitor MCP, Sentry 전체 팩, Spec-to-Code의 다중 에이전트 실행기는 추가하지 않았습니다. `cofa-reason`은 이 키트의 독립적인 경량 절차입니다. 모델 능력이나 완성률이 향상됐다는 측정 결과를 주장하지 않습니다.

README의 라이선스 예외와 각 파일의 선언을 확인하세요. 루트 MIT는 CC BY-SA 원본이나 그 각색본의 조건을 대체하지 않습니다.

## v1.4 범용 최적화와 서비스 구현

새 MIT 원본 두 곳: [combinatorial-optimization-skills](https://github.com/hajibabaie/combinatorial-optimization-skills)의 범용 SKILL.md 12개와 [scientific-agents](https://github.com/K-Dense-AI/scientific-agents)의 optimization-scientist SKILL.md 1개를 보관했습니다. 각 루트 LICENSE/LICENSE.md와 원문 바이트를 유지했습니다. 선택·제외 사유와 범위는 [OPTIMIZATION.ko.md](OPTIMIZATION.ko.md), 실제 참조 경로와 보정은 cofa-optimize의 source-guide에 있습니다.

`cofa-optimize`, `cofa-opt-service`, `cofa-explain`은 이 키트의 MIT 각색/연결 지침입니다. 원본을 그대로 활성화하거나 예제 결과로 실제 과제를 대체하지 않습니다. 버스 전용 스킬·검사기·전용 테스트는 v1.4에서 제거했습니다. 새 솔버 바이너리, 외부 계정/서비스, 완성 앱은 추가하지 않았습니다. 재시험 일정은 11월2일 사용자 전달 사항이며 원예선 PDF와 구분합니다.
