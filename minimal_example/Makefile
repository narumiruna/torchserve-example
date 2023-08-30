MODEL_STORE = model_store
MODEL_NAME = hello

archive:
	torch-model-archiver \
		--model-name ${MODEL_NAME} \
		--version 1.0 \
		--handler handler:hello \
		--export-path ${MODEL_STORE} \
		--force

start:
	torchserve \
		--start  \
		--model-store ${MODEL_STORE} \
		--models ${MODEL_NAME}.mar \
		--foreground
